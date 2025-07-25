# 💰 Quick Cash - Loan App

A modern, responsive loan application built with HTML, CSS, JavaScript, and Firebase.

## 🚀 Features

- **User Authentication** - Login/Register with mobile number
- **Complete User Profiles** - Comprehensive user data management
- **Loan Applications** - Apply for loans with EMI calculation
- **Firebase Integration** - Real-time data storage and authentication
- **Responsive Design** - Works on all devices
- **Session Management** - Track user sessions and device info
- **KYC Management** - Document verification system
- **Referral System** - Built-in referral code generation

## 📱 Screenshots

The app includes:
- Authentication page with login/register
- Home page with loan offers
- Profile management
- Loan application system

## 🔧 Quick Deployment

### Option 1: Netlify Drop (Easiest)
1. Go to [Netlify Drop](https://app.netlify.com/drop)
2. Drag and drop your `index.html` file
3. Your app is live instantly! 🎉

### Option 2: GitHub Pages
1. Create a new repository on GitHub
2. Upload `index.html` to the repository
3. Go to Settings → Pages
4. Select "Deploy from a branch" → main
5. Your app will be live at `https://yourusername.github.io/repository-name`

### Option 3: Firebase Hosting
```bash
npm install -g firebase-tools
firebase login
firebase init hosting
firebase deploy
```

### Option 4: Vercel
```bash
npm i -g vercel
vercel
```

### Option 5: Surge.sh
```bash
npx surge index.html
```

## 🛠️ Using the Deployment Script

Run the deployment helper:
```bash
./deploy.sh
```

This script provides multiple deployment options and guides you through the process.

## 🔥 Firebase Configuration

The app is already configured with Firebase. The configuration includes:
- Authentication
- Firestore Database
- Real-time updates

### Firebase Collections Structure:

#### `loanusers` Collection:
```javascript
{
  uid: "user-id",
  name: "User Name",
  mobile: "1234567890",
  email: "user@quickcash.app",
  personalDetails: { ... },
  addressDetails: { ... },
  kycDocuments: { ... },
  loanDetails: { ... },
  financialDetails: { ... },
  sessionInfo: { ... },
  timestamps: { ... }
}
```

#### `loans` Collection:
```javascript
{
  loanId: "LN123456",
  userId: "user-id",
  applicationNumber: "QC12345678",
  loanAmount: { requested: 500000, approved: 0 },
  loanTerms: { principalAmount, interestRate, monthlyEMI },
  status: { current: "pending", history: [...] },
  timestamps: { applied, submitted, lastUpdated }
}
```

## 📋 Features Included

### ✅ Authentication System
- Mobile-based registration
- Secure password authentication
- Session management
- Auto-redirect after login

### ✅ User Profile Management
- Complete profile forms
- KYC document tracking
- Address management
- Personal details

### ✅ Loan Application System
- EMI calculation
- Application tracking
- Status management
- Document requirements

### ✅ Dashboard Features
- Welcome banner
- Quick actions
- Loan offers
- Profile access

## 🎨 Customization

### Colors
The app uses CSS custom properties for easy theming:
```css
:root {
    --primary: #6c63ff;
    --secondary: #4a42e8;
    --accent: #ff6584;
    --success: #28a745;
}
```

### Firebase Config
Update the Firebase configuration in the script section:
```javascript
const firebaseConfig = {
    apiKey: "your-api-key",
    authDomain: "your-project.firebaseapp.com",
    projectId: "your-project-id",
    // ... other config
};
```

## 📱 Mobile Responsive

The app is fully responsive and works perfectly on:
- 📱 Mobile phones
- 📱 Tablets
- 💻 Desktop computers
- 🖥️ Large screens

## 🔒 Security Features

- Firebase Authentication
- Input validation
- XSS protection
- Secure data transmission
- Session management

## 📞 Support

For any issues or questions:
- Email: support@quickcash.com
- WhatsApp: +91 98765 43210
- Telegram: @quickcashsupport

## 📄 License

This project is for educational and commercial use.

---

## 🚀 Quick Start Commands

```bash
# Make deployment script executable
chmod +x deploy.sh

# Run deployment helper
./deploy.sh

# Or deploy directly to surge
npx surge index.html

# Or deploy to netlify
# Just drag index.html to https://app.netlify.com/drop
```

## 🌟 Live Demo

Upload your `index.html` to any of the platforms above and share the link!

**Happy Deploying! 🚀**