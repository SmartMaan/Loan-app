#!/bin/bash

# Quick Cash Loan App - Deployment Script
# This script helps you deploy your HTML file to various platforms

echo "🚀 Quick Cash Loan App - Deployment Helper"
echo "=========================================="

# Check if index.html exists
if [ ! -f "index.html" ]; then
    echo "❌ Error: index.html not found in current directory"
    exit 1
fi

echo "✅ Found index.html"
echo ""

# Show deployment options
echo "📦 Choose deployment option:"
echo "1. GitHub Pages (via git)"
echo "2. Netlify Drop (manual upload)"
echo "3. Vercel (via CLI)"
echo "4. Firebase Hosting"
echo "5. Copy to clipboard (for manual upload)"
echo "6. Create ZIP file for upload"
echo ""

read -p "Enter your choice (1-6): " choice

case $choice in
    1)
        echo "🔄 Deploying to GitHub Pages..."
        if [ -d ".git" ]; then
            git add .
            git commit -m "Update loan app - $(date)"
            git push origin main
            echo "✅ Pushed to GitHub. Enable GitHub Pages in repository settings."
        else
            echo "❌ Not a git repository. Initialize with: git init"
        fi
        ;;
    2)
        echo "🌐 For Netlify Drop:"
        echo "1. Go to https://app.netlify.com/drop"
        echo "2. Drag and drop your index.html file"
        echo "3. Your app will be live instantly!"
        ;;
    3)
        echo "⚡ For Vercel deployment:"
        echo "1. Install Vercel CLI: npm i -g vercel"
        echo "2. Run: vercel"
        echo "3. Follow the prompts"
        if command -v vercel &> /dev/null; then
            read -p "Deploy now? (y/n): " deploy_now
            if [ "$deploy_now" = "y" ]; then
                vercel
            fi
        fi
        ;;
    4)
        echo "🔥 For Firebase Hosting:"
        echo "1. Install Firebase CLI: npm install -g firebase-tools"
        echo "2. Run: firebase login"
        echo "3. Run: firebase init hosting"
        echo "4. Run: firebase deploy"
        ;;
    5)
        echo "📋 Copying HTML content to clipboard..."
        if command -v pbcopy &> /dev/null; then
            cat index.html | pbcopy
            echo "✅ HTML content copied to clipboard (macOS)"
        elif command -v xclip &> /dev/null; then
            cat index.html | xclip -selection clipboard
            echo "✅ HTML content copied to clipboard (Linux)"
        elif command -v clip &> /dev/null; then
            cat index.html | clip
            echo "✅ HTML content copied to clipboard (Windows)"
        else
            echo "❌ Clipboard tool not found. Please copy index.html content manually."
        fi
        ;;
    6)
        echo "📦 Creating ZIP file..."
        zip -r quickcash-loan-app.zip index.html
        echo "✅ Created quickcash-loan-app.zip"
        echo "📤 Upload this ZIP file to your hosting platform"
        ;;
    *)
        echo "❌ Invalid choice. Please run the script again."
        ;;
esac

echo ""
echo "🌟 Quick Upload Options:"
echo "• Netlify Drop: https://app.netlify.com/drop"
echo "• Surge.sh: npx surge index.html"
echo "• GitHub Pages: Push to repository and enable Pages"
echo "• CodePen: Copy HTML content to CodePen"
echo ""
echo "✨ Your loan app is ready to deploy!"