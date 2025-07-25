#!/usr/bin/env python3
"""
Quick Cash Loan App - Python Deployment Helper
Helps you deploy your HTML file to various platforms
"""

import os
import sys
import subprocess
import webbrowser
import zipfile
import shutil
from pathlib import Path

def check_file_exists():
    """Check if index.html exists"""
    if not os.path.exists('index.html'):
        print("❌ Error: index.html not found in current directory")
        return False
    print("✅ Found index.html")
    return True

def create_zip():
    """Create a ZIP file for upload"""
    print("📦 Creating ZIP file...")
    with zipfile.ZipFile('quickcash-loan-app.zip', 'w') as zipf:
        zipf.write('index.html')
        if os.path.exists('README.md'):
            zipf.write('README.md')
    print("✅ Created quickcash-loan-app.zip")
    print("📤 Upload this ZIP file to your hosting platform")

def copy_to_clipboard():
    """Copy HTML content to clipboard"""
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Try different clipboard methods based on OS
        if sys.platform == "darwin":  # macOS
            process = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
            process.communicate(content.encode('utf-8'))
            print("✅ HTML content copied to clipboard (macOS)")
        elif sys.platform == "linux":  # Linux
            try:
                process = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
                process.communicate(content.encode('utf-8'))
                print("✅ HTML content copied to clipboard (Linux)")
            except FileNotFoundError:
                print("❌ xclip not found. Install with: sudo apt-get install xclip")
        elif sys.platform == "win32":  # Windows
            try:
                import pyperclip
                pyperclip.copy(content)
                print("✅ HTML content copied to clipboard (Windows)")
            except ImportError:
                print("❌ pyperclip not found. Install with: pip install pyperclip")
        else:
            print("❌ Clipboard not supported on this platform")
            
    except Exception as e:
        print(f"❌ Error copying to clipboard: {e}")

def deploy_surge():
    """Deploy using Surge.sh"""
    print("⚡ Deploying to Surge.sh...")
    try:
        # Check if surge is installed
        subprocess.run(['surge', '--version'], check=True, capture_output=True)
        
        # Deploy
        result = subprocess.run(['surge', 'index.html'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Deployed to Surge.sh successfully!")
            print("🌐 Your app is live!")
        else:
            print("❌ Surge deployment failed")
            print(result.stderr)
    except subprocess.CalledProcessError:
        print("❌ Surge CLI not found. Install with: npm install -g surge")
    except FileNotFoundError:
        print("❌ Node.js/npm not found. Please install Node.js first")

def init_git_repo():
    """Initialize git repository and push to GitHub"""
    print("🔄 Setting up Git repository...")
    try:
        # Initialize git if not already
        if not os.path.exists('.git'):
            subprocess.run(['git', 'init'], check=True)
            print("✅ Git repository initialized")
        
        # Add files
        subprocess.run(['git', 'add', '.'], check=True)
        
        # Commit
        subprocess.run(['git', 'commit', '-m', 'Initial commit - Quick Cash Loan App'], check=True)
        
        print("✅ Files committed to git")
        print("📝 Next steps:")
        print("1. Create a repository on GitHub")
        print("2. Run: git remote add origin <your-repo-url>")
        print("3. Run: git push -u origin main")
        print("4. Enable GitHub Pages in repository settings")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Git error: {e}")
    except FileNotFoundError:
        print("❌ Git not found. Please install Git first")

def open_deployment_sites():
    """Open deployment websites in browser"""
    sites = [
        ("Netlify Drop", "https://app.netlify.com/drop"),
        ("Vercel", "https://vercel.com/new"),
        ("GitHub", "https://github.com/new"),
        ("CodePen", "https://codepen.io/pen/"),
        ("JSFiddle", "https://jsfiddle.net/")
    ]
    
    print("🌐 Opening deployment sites in browser...")
    for name, url in sites:
        print(f"Opening {name}...")
        webbrowser.open(url)

def show_manual_instructions():
    """Show manual deployment instructions"""
    print("""
🌟 Manual Deployment Options:

1. 📁 Netlify Drop (Easiest):
   • Go to: https://app.netlify.com/drop
   • Drag and drop your index.html file
   • Instant deployment!

2. 🚀 Vercel:
   • Go to: https://vercel.com/new
   • Import your project or upload files
   • Follow the setup wizard

3. 📚 GitHub Pages:
   • Create repository on GitHub
   • Upload index.html
   • Settings → Pages → Deploy from branch

4. ⚡ Surge.sh:
   • Run: npx surge index.html
   • Follow the prompts

5. 🔥 Firebase Hosting:
   • npm install -g firebase-tools
   • firebase login
   • firebase init hosting
   • firebase deploy

6. 📝 CodePen/JSFiddle:
   • Copy HTML content
   • Paste into online editor
   • Save and share
""")

def main():
    """Main function"""
    print("🚀 Quick Cash Loan App - Python Deployment Helper")
    print("=" * 50)
    
    if not check_file_exists():
        return
    
    print("\n📦 Choose deployment option:")
    print("1. Create ZIP file for manual upload")
    print("2. Copy HTML to clipboard")
    print("3. Deploy to Surge.sh")
    print("4. Setup Git repository")
    print("5. Open deployment sites in browser")
    print("6. Show manual instructions")
    print("7. Do everything (ZIP + Clipboard + Open sites)")
    
    try:
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "1":
            create_zip()
        elif choice == "2":
            copy_to_clipboard()
        elif choice == "3":
            deploy_surge()
        elif choice == "4":
            init_git_repo()
        elif choice == "5":
            open_deployment_sites()
        elif choice == "6":
            show_manual_instructions()
        elif choice == "7":
            print("🚀 Doing everything...")
            create_zip()
            copy_to_clipboard()
            open_deployment_sites()
            show_manual_instructions()
        else:
            print("❌ Invalid choice. Please run the script again.")
            
    except KeyboardInterrupt:
        print("\n👋 Deployment cancelled by user")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print("\n✨ Your loan app is ready to deploy!")
    print("🌟 Choose any of the options above to get your app live!")

if __name__ == "__main__":
    main()