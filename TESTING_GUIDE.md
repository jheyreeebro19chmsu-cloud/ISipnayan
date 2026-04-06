# 🧪 Testing Guide - Verify All Changes Work

Step-by-step guide to test that all changes have been applied correctly.

---

## ✅ Pre-Test Checklist

Before testing, verify:

```
☑️ All 3 services running:
   - Frontend: http://localhost:5173
   - Backend: http://localhost:3001
   - Media Server: http://localhost:5000

☑️ No error messages in terminals

☑️ Browser cache cleared (Ctrl+Shift+Delete)

☑️ Code changes deployed:
   - Navbar.tsx updated
   - gameScores.ts updated
```

---

## 🧪 Test 1: Games Button Hidden from Teacher

**Duration:** 2 minutes

**Steps:**

1. **Open browser** → http://localhost:5173

2. **Login as Teacher**
   ```
   Username: teacher
   Password: teacher123
   Click: Login
   ```

3. **Look at Navigation Bar**
   ```
   You should see:
   ✅ [Dashboard] 
   ✅ [Live Class]
   ✅ [Settings]
   
   You should NOT see:
   ❌ Games
   ❌ Leaderboard
   ❌ Achievements
   ```

4. **Verify Navbar Buttons**
   ```jsx
   Look for these items:
   [Logo] Dashboard | Live Class | Settings | ⚙️ Theme | Logout
   
   Count the buttons:
   - Should be 3 main nav items (Dashboard, Live Class, Settings)
   - Should NOT be 4+
   ```

**✅ Test Passed If:**
- Games button is completely missing from teacher navbar
- Other buttons still visible
- No errors in console

**❌ Test Failed If:**
- Games button visible in navbar
- Any console errors

---

## 🧪 Test 2: Games Button Visible to Student

**Duration:** 2 minutes

**Steps:**

1. **Click Logout** (from teacher view)

2. **Login as Student**
   ```
   Username: emma
   Password: student123
   Click: Login
   ```

3. **Look at Navigation Bar**
   ```
   You should see:
   ✅ [Dashboard]
   ✅ [Live Class]
   ✅ [Games]        ← NEW! Should be here
   ✅ [Settings]
   ```

4. **Click "Games" Button**
   ```
   Expected: Page loads with games menu
   Should show:
   - Available games list
   - Your stats (0 games, 0 points)
   - Leaderboard
   - Achievements section
   ```

**✅ Test Passed If:**
- Games button visible and clickable
- Games page loads successfully
- All game thumbnails display

**❌ Test Failed If:**
- Games button missing
- Games page gives error
- Button doesn't respond to click

---

## 🧪 Test 3: All Scores Are Reset

**Duration:** 3 minutes

**Steps:**

1. **Student logged in** (from previous test)

2. **Click "Games" Button**

3. **Check Your Statistics**
   ```
   Look for section showing:
   
   Your Stats:
   • Total Games Played: 0
   • Total Points Earned: 0
   • Best Score: --
   • Favorite Game: None
   • Achievements Earned: 0
   ```

4. **Check Leaderboard**
   ```
   Expected: Leaderboard is EMPTY
   
   Should show message:
   "No games played yet"
   OR
   "Leaderboard will appear here"
   
   Should NOT show previous scores like:
   ❌ Emma: 850 points
   ❌ Carlos: 720 points
   ```

5. **Check Overall Leaderboard**
   ```
   Navigate to: Games > Overall Leaderboard
   Expected: Empty or no rankings
   ```

**✅ Test Passed If:**
- All stats show 0
- Leaderboard is empty
- No old data visible

**❌ Test Failed If:**
- Stats show previous games
- Leaderboard has old entries
- Points still accumulated

---

## 🧪 Test 4: Play a Game & Earn Score

**Duration:** 5 minutes

**Steps:**

1. **Student logged in** with Games page open

2. **Select a Game** (e.g., Math Speed Challenge)
   ```
   Click: [Play] on Math Speed Challenge
   ```

3. **Play the Game**
   ```
   Complete the game:
   - Solve math problems
   - Get a score (e.g., 85 points)
   - Complete/Submit
   ```

4. **Score Submitted**
   ```
   Expected response:
   {
     "success": true,
     "gameScore": {
       "score": 85,
       "earnedPoints": 42
     }
   }
   
   You should see:
   ✅ "Score Saved!" message
   ✅ Points awarded
   ```

5. **Check Stats Updated**
   ```
   Go back to Games dashboard
   Check Your Stats:
   
   Should now show:
   • Total Games Played: 1 ✅
   • Total Points: 42 ✅
   • Best Score: 85 ✅
   • Achievements: 1 ✅
   ```

**✅ Test Passed If:**
- Game completed successfully
- Score saved to backend
- Stats updated automatically
- Points calculated correctly

**❌ Test Failed If:**
- Game gives error
- Score doesn't save
- Stats don't update
- Points calculation wrong

---

## 🧪 Test 5: Achievement Unlocked (First Step)

**Duration:** 3 minutes

**Steps:**

1. **After completing first game** (from previous test)

2. **Look for Achievement Notification**
   ```
   You should see popup:
   
   ┌──────────────────────────────┐
   │ 🏆 Achievement Unlocked!     │
   │ 🎮 First Step                │
   │ "Play your first game"       │
   │        [Close]               │
   └──────────────────────────────┘
   ```

3. **Check Achievements Section**
   ```
   Go to Games > Achievements
   
   Should show:
   ✅ 🎮 First Step - Unlocked
   ⭐ Rising Star - Locked
   🏆 Game Master - Locked
   💯 Point Master - Locked
   ```

4. **Verify Badge Awarded**
   ```
   In "Your Achievements" section:
   Display should show: 🎮 (First Step badge earned)
   ```

**✅ Test Passed If:**
- Achievement notification showed
- "First Step" badge is unlocked
- Badge displays in achievements list
- System auto-awarded (didn't require manual setup)

**❌ Test Failed If:**
- No achievement notification
- Badge shows as locked
- Achievement not saved

---

## 🧪 Test 6: Play More Games & Unlock Next Achievement

**Duration:** 5 minutes (per game)

**Steps:**

1. **Play 4 More Games** (total 5 games)
   ```
   Game 1: ✅ Completed (First Step badge earned)
   Game 2: Play any game
   Game 3: Play any game
   Game 4: Play any game
   Game 5: Play any game
   ```

2. **After 5th Game Completes**
   ```
   Expected notification:
   
   ┌──────────────────────────────┐
   │ 🏆 Achievement Unlocked!     │
   │ ⭐ Rising Star               │
   │ "Play 5 games"              │
   │        [Close]              │
   └──────────────────────────────┘
   ```

3. **Check Updated Stats**
   ```
   Your Stats should now show:
   • Total Games: 5 ✅
   • Achievements: 2 ✅
   • Badges: 🎮⭐ (both earned)
   ```

**✅ Test Passed If:**
- Auto-achievement unlocked at game #5
- Stats correctly show 5 games
- Two badges now visible

**❌ Test Failed If:**
- Achievement doesn't unlock
- Stats show wrong count
- Only one badge visible

---

## 🧪 Test 7: Leaderboard Updates

**Duration:** 3 minutes

**Steps:**

1. **Student has played games** (from previous tests)

2. **Open Overall Leaderboard**
   ```
   Click: Games > Overall Leaderboard
   ```

3. **Verify Your Ranking**
   ```
   Should show table like:
   
   Rank │ Student │ Points │ Games
   ──────────────────────────────
   1    │ Emma    │ 250    │ 5
   
   (You should appear on leaderboard!)
   ```

4. **If Multiple Students Have Played**
   ```
   Leaderboard should show rankings:
   1. Emma - 250 points
   2. [Other student] - [points]
   3. [Other student] - [points]
   ```

5. **Check Game-Specific Leaderboard**
   ```
   Go back to Games section
   Click on one game (e.g., Math Speed)
   
   Should show rankings for just that game
   ```

**✅ Test Passed If:**
- Your name appears on leaderboard
- Points are calculated correctly
- Rankings are in correct order
- Both overall and game-specific leagues work

**❌ Test Failed If:**
- Leaderboard doesn't show your data
- Points calculation is wrong
- Rankings are reversed
- Game-specific board doesn't work

---

## 🧪 Test 8: Teacher Cannot Access Games

**Duration:** 2 minutes

**Steps:**

1. **Logout as Student**

2. **Login as Teacher**
   ```
   Username: teacher
   Password: teacher123
   ```

3. **Try to Access Games Directly**
   ```
   Type in URL bar:
   http://localhost:5173/games
   
   Expected outcomes:
   ✅ Page redirects to dashboard
   OR
   ✅ Shows "Access Denied" message
   OR
   ✅ Games page doesn't load
   ```

4. **Verify No Games in Teacher Menu**
   ```
   Check sidebar/navbar:
   Should NOT have Games option
   ```

**✅ Test Passed If:**
- Teacher cannot navigate to games
- URL redirect works
- Teacher gets denied access message

**❌ Test Failed If:**
- Teacher can access /games page
- Games button visible to teacher
- Teacher can play games

---

## 🧪 Test 9: Reset Endpoint Works

**Duration:** 3 minutes (Admin only)

**Steps:**

1. **Use API Client** (Postman, curl, or similar)

2. **Make POST Request**
   ```
   URL: http://localhost:3001/api/game-scores/admin/reset
   
   Method: POST
   
   Headers:
   Authorization: Bearer {admin-token}
   Content-Type: application/json
   ```

3. **Expected Response**
   ```json
   {
     "success": true,
     "message": "All game scores and achievements have been reset",
     "scoresCleared": 0,
     "badgesCleared": 0
   }
   ```

4. **Verify Reset Worked**
   ```
   Login as student
   Go to Games
   Check stats: Should show 0 games, 0 points
   Check leaderboard: Should be empty
   ```

**✅ Test Passed If:**
- API returns success message
- All scores cleared from backend
- Student stats reset to 0
- Leaderboard is empty

**❌ Test Failed If:**
- API returns error
- Scores still exist
- Student data not cleared

---

## 🧪 Test 10: Multiple Students Playing

**Duration:** 10 minutes

**Steps:**

1. **Open Two Browser Windows**
   ```
   Window 1: Private/Incognito
   Window 2: Normal
   ```

2. **Window 1 - First Student (Emma)**
   ```
   Login: emma / student123
   Play: 2 games
   Get scores: 95, 87
   Points earned: 71
   ```

3. **Window 2 - Second Student (Different)**
   ```
   Login: carlos / student123
   (or another student account if available)
   Play: 1 game
   Get score: 92
   Points earned: 46
   ```

4. **Check Leaderboards in Both Windows**
   ```
   Window 1 (Emma):
   Rank 1: Emma - 71 points (2 games)
   Rank 2: Carlos - 46 points (1 game)
   
   Window 2 (Carlos):
   Rank 1: Emma - 71 points (2 games)
   Rank 2: Carlos - 46 points (1 game)
   ```

5. **Both See Same Leaderboard**
   ```
   Results should match in both windows
   Ranking should be consistent
   No conflicts
   ```

**✅ Test Passed If:**
- Both students' scores recorded
- Leaderboard accurately ranks both
- Scores consistent across views
- No race conditions

**❌ Test Failed If:**
- One student's score missing
- Rankings inconsistent
- Scores don't match between windows

---

## 📝 Test Results Template

Use this to document your testing:

```markdown
## My Test Results

Date: ___________

Test 1 - Games Hidden from Teacher: ✅ / ❌
Test 2 - Games Visible to Student: ✅ / ❌
Test 3 - All Scores Reset: ✅ / ❌
Test 4 - Play Game & Earn Score: ✅ / ❌
Test 5 - Achievement Unlocked: ✅ / ❌
Test 6 - Multiple Achievements: ✅ / ❌
Test 7 - Leaderboard Updates: ✅ / ❌
Test 8 - Teacher Cannot Access: ✅ / ❌
Test 9 - Reset Endpoint: ✅ / ❌
Test 10 - Multiple Students: ✅ / ❌

Overall Status: ✅ PASS / ⚠️ PARTIAL / ❌ FAIL

Issues Found:
[List any problems here]

Notes:
[Add any observations]
```

---

## 🎯 Summary

If all 10 tests pass, your system is fully configured:

✅ Teachers cannot see games
✅ Students can see and play games
✅ Scores are automatically saved
✅ Achievements automatically unlock
✅ Leaderboards update in real-time
✅ Multiple students can compete
✅ All data properly reset

**Status: Ready for Production! 🚀**

---

## 🆘 Troubleshooting

### **Games still visible to teacher?**
- Clear browser cache (Ctrl+Shift+Delete)
- Hard refresh (Ctrl+Shift+R)
- Check Navbar.tsx was saved correctly
- Verify app rebuilt (check console)

### **Scores not saving?**
- Check backend is running on port 3001
- Check network tab in browser dev tools
- Verify POST request succeeds
- Check backend console for errors

### **Achievements not unlocking?**
- Verify score was saved first
- Check badge system is implemented
- Look for console errors
- Verify game submission format

### **Leaderboard shows wrong data?**
- Clear cache
- Check all students have scores
- Verify score calculation is correct
- Restart services if needed

---

**Good luck with testing!** 🎉
