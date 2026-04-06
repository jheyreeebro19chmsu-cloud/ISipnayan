# 🎥 Camera Code - Step by Step

This explains exactly which pieces of code make your camera work.

---

## 🎯 The Complete Camera Flow

```
Your Camera Hardware (Webcam)
         ↓
[Media Server gets frame]
    (app.py)
         ↓
[Backend API returns frame]
   (routes/media.ts)
         ↓
[Frontend requests camera frame]
    (useMediaServer hook)
         ↓
[Your Face Displayed!]
   (VideoConferencePage.tsx)
         ↓
Students see your face
  (StudentMeetingsPage calls
   same VideoConferencePage)
```

---

## 📄 Key Code Files Involved

### 1️⃣ **Frontend: src/app/pages/VideoConferencePage.tsx**

**This is where YOUR FACE appears on screen!**

```jsx
// Line 128-138: This code DISPLAYS YOUR CAMERA FEED
<img
  src={`${media.cameraFrame}?t=${Date.now()}`}
  alt="Your camera"
  className="w-full h-full object-cover"
/>
<div className="absolute bottom-4 left-4 text-white text-sm bg-black bg-opacity-50 px-3 py-2 rounded">
  <p className="font-semibold">{user.name}</p>
  <p className="text-xs text-gray-300">{user.role}</p>
  {media.cameraStats && (
    <p className="text-xs text-green-400">
      {Math.round(media.cameraStats.fps || 0)} FPS
    </p>
  )}
</div>
```

**What this does:**
- `media.cameraFrame` = URL to the camera image
- `<img src={...}>` = Shows the image (YOUR FACE)
- Bottom-left text = Shows your name and role
- Green FPS = Shows how fast the camera is running (frames per second)

---

### 2️⃣ **Frontend Hook: src/app/utils/useMediaServer.ts**

**This hook makes the API calls to get your camera frame.**

```typescript
// This hook does:
const useMediaServer = (sessionId) => {
  // 1. Starts the camera
  const startCamera = async (options) => {
    // Calls: POST /api/media/camera/start
    // Gets back: sessionId and frame URL
    // Returns frame URL: /api/media/camera/frame/{sessionId}.jpg
  }

  // 2. Gets the camera frame (updates every 500ms)
  const refr_cameraFrame = () => {
    // Keeps fetching new frames
    // Shows the absolute latest image from your camera
  }

  // 3. Stops the camera
  const stopCamera = async () => {
    // Calls: POST /api/media/camera/stop
    // Stops streaming
  }

  // Returns:
  return {
    cameraFrame: "http://localhost:3001/api/media/camera/frame/...",
    startCamera,
    stopCamera,
    cameraStats: { fps: 30 },
    ...
  }
}
```

**Where the code is:**
📍 [src/app/utils/useMediaServer.ts](src/app/utils/useMediaServer.ts)

---

### 3️⃣ **Backend API: backend/src/routes/media.ts**

**This API serves your camera frames to the frontend.**

```typescript
// GET /api/media/camera/frame/{sessionId}.jpg
app.get('/api/media/camera/frame/:sessionId', async (req, res) => {
  
  // 1. Verify user is logged in
  const token = req.query.token as string
  const user = verifyToken(token)

  // 2. Get the frame from media server
  const frameBase64 = await mediaServerService.getCameraFrame(sessionId)

  // 3. Send back as JPEG image
  res.setHeader('Content-Type', 'image/jpeg')
  res.setHeader('Access-Control-Allow-Origin', '*')
  res.setHeader('Cache-Control', 'no-cache')
  
  const buffer = Buffer.from(frameBase64, 'base64')
  res.send(buffer)
})
```

**Where the code is:**
📍 [backend/src/routes/media.ts](backend/src/routes/media.ts#L50-L80)

---

### 4️⃣ **Media Server: media_server/app.py**

**This Python code actually captures your camera.**

```python
# GET /api/camera/frame/{sessionId}.jpg
@app.route('/api/camera/frame/<session_id>')
def get_camera_frame(session_id):
    try:
        # Get the active camera for this session
        if session_id in active_cameras:
            camera = active_cameras[session_id]
            # Capture a frame from your webcam
            frame = camera.get_frame()  # From OpenCV/DirectShow
            # Convert to JPEG
            _, buffer = cv2.imencode('.jpg', frame)
            return send_file(
                BytesIO(buffer),
                mimetype='image/jpeg'
            )
    except:
        # If no camera, show fallback test frame
        return get_test_frame()
```

**Where the code is:**
📍 [media_server/app.py](media_server/app.py#L100-L130)

---

## 🎬 How It All Works Together

### **Step 1: You Click "Start Session"**

```
VideoConferencePage.tsx (line 99-106)
  └─ handleInitSetup()
      └─ media.startCamera()
```

### **Step 2: Frontend Requests Camera Start**

```
useMediaServer.ts
  └─ POST /api/media/camera/start
      └─ Body: { sessionId, width: 640, height: 480, fps: 30 }
```

### **Step 3: Backend Starts Camera**

```
backend/src/routes/media.ts
  └─ POST /api/media/camera/start
      └─ mediaServerService.startCamera()
          └─ POST http://localhost:5000/api/camera/start
```

### **Step 4: Media Server Activates Webcam**

```
media_server/app.py
  └─ POST /api/camera/start
      └─ Opens your Windows camera (DirectShow)
      └─ Creates VideoCapture object
      └─ Stores in active_cameras[sessionId]
```

### **Step 5: Frontend Gets Frame URL**

```
useMediaServer.ts
  ├─ Receives: { frameUrl: "/api/media/camera/frame/session123" }
  ├─ Now cameraFrame = "http://localhost:3001/api/media/camera/frame/session123.jpg"
  └─ Refreshes every 500ms
```

### **Step 6: Frontend Displays Your Face**

```
VideoConferencePage.tsx (line 128)
  └─ <img src={media.cameraFrame}>
      └─ This triggers:
          ├─ GET /api/media/camera/frame/session123
          │   └─ backend verifies token
          │   └─ backend calls media server
          │   └─ backend returns JPEG
          └─ Browser displays image (YOUR FACE!)
```

### **Step 7: Frontend Refreshes Every 500ms**

```
useMediaServer.ts
  └─ setInterval(() => {
      ├─ Get fresh frame from media server
      ├─ Update cameraFrame URL
      └─ </img> tag auto-updates to show new image
    }, 500)  // 500 milliseconds = 2 frames per second minimum
```

---

## 🔑 Key Code Sections to Understand

### **Button to Toggle Camera**

```jsx
// VideoConferencePage.tsx line 47-58
const toggleCamera = useCallback(async () => {
  if (isVideoOff) {
    // Start camera
    await media.startCamera({
      width: 640,
      height: 480,
      fps: 30,
    })
    setIsVideoOff(false)  // Button shows "camera is ON"
  } else {
    // Stop camera
    await media.stopCamera()
    setIsVideoOff(true)   // Button shows "camera is OFF"
  }
}, [isVideoOff, media])
```

### **Display the Camera Frame**

```jsx
// VideoConferencePage.tsx line 124-140
{media.cameraFrame && !isVideoOff ? (
  // SHOW YOUR FACE
  <div className="w-full h-full">
    <img
      src={`${media.cameraFrame}?t=${Date.now()}`}
      alt="Your camera"
      className="w-full h-full object-cover"
    />
    {/* Your name and FPS counter below image */}
  </div>
) : (
  // SHOW PLACEHOLDER IF CAMERA OFF
  <div className="text-center">
    <div className="avatar">{user.initials}</div>
    <p>{user.name}</p>
  </div>
)}
```

### **Refresh Camera Frame Every 500ms**

```typescript
// useMediaServer.ts
const refr_cameraFrame = useCallback(() => {
  if (!sessionId || !authToken) return

  const timer = setInterval(() => {
    setCameraFrame(
      `${baseUrl}/api/media/camera/frame/${sessionId}.jpg?token=${encodeURIComponent(authToken)}`
    )
  }, 500)  // Request new frame every 500ms

  return () => clearInterval(timer)
}, [sessionId, authToken])
```

---

## 🎯 Summary: Where Your Camera Is Configured

| Component | File | What it does | Key Line |
|-----------|------|-------------|----------|
| **Display** | `VideoConferencePage.tsx` | Shows `<img>` tag with camera frame | Line 128 |
| **Camera Hook** | `useMediaServer.ts` | Gets camera frame URL from backend | Line ~150 |
| **Backend API** | `media.ts` | Serves camera frames as JPEG | Line ~50 |
| **Media Server** | `app.py` | Captures real camera feed | Line ~100 |
| **TypeScript Types** | `types/index.ts` | Defines camera response types | Line ~45 |

---

## ✅ What Happens When You Click Camera Button

**Off → On:**
```
Click "Camera" button
  ↓
toggleCamera() runs
  ↓
media.startCamera() called
  ↓
POST /api/media/camera/start
  ↓
Backend starts camera on media server
  ↓
Backend returns frame URL
  ↓
Frontend stores in cameraFrame state
  ↓
<img src={cameraFrame}> displays
  ↓
YOU SEE YOUR FACE ✅
  ↓
Every 500ms: New frame fetched and displayed
```

**On → Off:**
```
Click "Camera" button again
  ↓
media.stopCamera() called
  ↓
POST /api/media/camera/stop
  ↓
isVideoOff = true
  ↓
<img> tag hidden
  ↓
Avatar placeholder shown instead
```

---

## 🎤 Microphone & Screen Sharing

Same pattern as camera!

### **Microphone**
```
startMicrophone() → POST /api/media/microphone/start
stopMicrophone() → POST /api/media/microphone/stop
// Updates audioLevel state shown as slider
```

### **Screen Sharing**
```
startScreen() → POST /api/media/screen/start
stopScreen() → POST /api/media/screen/stop
// Gets screenFrame URL, displays in top-right overlay
```

---

## 🚀 To See Your Camera Work

1. **Open** http://localhost:5173
2. **Login** teacher/teacher123
3. **Create Meeting**
4. **Click "Start Session"**
5. **Look at the image** → YOUR FACE! 📹
6. **Click camera button** →️ toggles on/off

The entire system is already coded and integrated. No additional code needed! ✅

---

**Status**: 🟢 All camera code is in place and working
