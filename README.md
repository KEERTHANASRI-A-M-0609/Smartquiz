# Smartquiz
Built an interactive quiz platform supporting subject-wise quizzes, multiple difficulty levels, real-time timers, and instant feedback to enhance learning engagement. Implemented features such as user authentication, hints, retry options, leaderboards, and performance tracking to improve user experience and learning outcomes.


## 🌟 Features

### 🎮 Core Functionality
- **🎓 Multi-Subject Quizzes**: Mathematics, Science, History, Geography, Literature
- **🔀 Mixed Quiz Mode**: Combines questions from all subjects for ultimate challenge
- **⏱️ Timer System**: 30-second countdown per question with visual feedback
- **📊 Progress Tracking**: Real-time question progress and performance analytics
- **🎯 Difficulty Levels**: Easy, Medium, and Hard questions for varied challenge
- **📈 Score Analytics**: Detailed performance feedback with percentage calculations

### 🎨 User Interface
- **✨ Professional Design**: Modern color scheme with intuitive navigation
- **🎨 Visual Feedback**: Color-coded answer highlighting (Green ✅ / Red ❌)
- **📱 Responsive Layout**: Clean, organized interface that scales beautifully
- **⚡ Real-time Updates**: Dynamic timer and progress indicators

### 🔧 Technical Features
- **🏗️ Object-Oriented Architecture**: Clean, maintainable code structure
- **🎲 Random Question Selection**: Ensures unique quiz experiences every time
- **🔄 State Management**: Robust handling of quiz states and user interactions
- **🛡️ Error Handling**: Comprehensive timer management and input validation

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.6 or higher (Tkinter included)
```

### Installation & Run
```bash
# Clone the repository
git clone https://github.com/yourusername/enhanced-quiz-app.git

# Navigate to project directory
cd enhanced-quiz-app

# Run the application
python enhanced_quiz_app.py
```

## 🎮 How to Play

1. **🏠 Launch**: Run the application to see the main menu
2. **📚 Choose Subject**: Select from 5 subjects or try Mixed Quiz mode
3. **⏰ Answer Quickly**: Each question has a 30-second timer
4. **📊 View Results**: Get detailed performance feedback after completion
5. **🔄 Play Again**: Return to menu for another round

## 📚 Quiz Categories

| Subject | Topics Covered | Question Count |
|---------|---------------|----------------|
| 🔢 **Mathematics** | Algebra, Calculus, Geometry | 5+ questions |
| 🔬 **Science** | Physics, Chemistry, Biology | 5+ questions |
| 🏛️ **History** | World Wars, Historical Figures | 5+ questions |
| 🌍 **Geography** | Countries, Landmarks, Features | 5+ questions |
| 📖 **Literature** | Classic Authors, Famous Works | 5+ questions |

## 🏗️ Project Structure

```
enhanced-quiz-app/
│
├── enhanced_quiz_app.py    # Main application file
├── README.md              # Project documentation
└── screenshots/           # Application screenshots
    ├── main_menu.png
    ├── quiz_interface.png
    └── results_screen.png
```

## 💻 Code Architecture

```python
class QuizApp:
    ├── 🎯 Quiz Management
    │   ├── setup_main_menu()     # Main interface
    │   ├── start_quiz()          # Subject selection
    │   └── start_mixed_quiz()    # Mixed mode
    │
    ├── 🎮 Game Logic
    │   ├── display_question()    # Question rendering
    │   ├── check_answer()        # Answer validation
    │   └── show_results()        # Score display
    │
    └── ⏱️ Timer System
        ├── start_timer()         # Timer initialization
        ├── update_timer()        # Real-time updates
        └── time_up()            # Timeout handling
```

## 🎨 Design System

### Color Palette
```css
Primary Blue:    #3498db  /* Buttons, accents */
Dark Gray:       #34495e  /* Headers, text */
Success Green:   #27ae60  /* Correct answers */
Warning Orange:  #f39c12  /* Good performance */
Error Red:       #e74c3c  /* Wrong answers */
Light Gray:      #ecf0f1  /* Background */
```

### Typography
- **Headers**: Arial Bold, 24px
- **Questions**: Arial Regular, 16px  
- **Buttons**: Arial Regular, 12px
- **Timer**: Arial Bold, 14px

## 📊 Performance Metrics

| Score Range | Performance | Feedback |
|-------------|-------------|----------|
| 80-100% | 🏆 Excellent | Outstanding performance! |
| 60-79% | 👍 Good | Well done! |
| 0-59% | 📚 Practice | Keep practicing! |

## 🔧 Customization

### Adding New Questions
```python
"New Subject": [
    {
        "question": "Your question here?",
        "choices": ["Option A", "Option B", "Option C", "Option D", "Option E"],
        "answer": "Correct Option",
        "difficulty": "Easy"  # Easy/Medium/Hard
    }
]
```

### Modifying Settings
```python
self.time_limit = 30        # Timer duration (seconds)
question_count = 5          # Questions per subject
mixed_count = 10           # Questions in mixed mode
```

## 🚀 Future Enhancements

- [ ] 💾 Database integration for persistent storage
- [ ] 👥 User profiles and progress tracking
- [ ] 🌐 Multiplayer quiz battles
- [ ] 🧠 Adaptive difficulty based on performance
- [ ] 🔊 Audio feedback and sound effects
- [ ] 📱 Mobile-responsive web version
- [ ] 📄 Export results to PDF reports
- [ ] 🏆 Achievement system and badges

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
6. 
