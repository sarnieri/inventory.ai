# Inventory.AI Website

Static website files for Inventory.AI app - Support, Privacy Policy, and Terms & Conditions pages in 11 languages.

## 📁 Structure

```
website/
├── index.html                 # Main entry point (auto-detects language)
├── index-{lang}.html          # Homepage for each language
├── support-{lang}.html        # Support page
├── privacy-{lang}.html        # Privacy Policy
├── terms-{lang}.html          # Terms & Conditions
└── README.md                  # This file
```

## 🌍 Supported Languages

- **en** - English
- **it** - Italian
- **de** - German
- **es** - Spanish
- **fr** - French
- **ja** - Japanese
- **ko** - Korean
- **nl** - Dutch
- **pt** - Portuguese
- **ru** - Russian
- **zh** - Chinese (Simplified)

## 🚀 Deployment Options

### Option 1: GitHub Pages (Recommended)

1. Create a new repository: `garagevault-website`
2. Upload all HTML files to the repository
3. Go to Settings > Pages
4. Enable GitHub Pages from the main branch
5. Your site will be available at: `https://yourusername.github.io/garagevault-website`

### Option 2: Netlify

1. Go to [netlify.com](https://netlify.com)
2. Drag and drop the entire `website` folder
3. Your site will be live at: `https://garagevault.netlify.app` (or custom domain)

### Option 3: Vercel

1. Go to [vercel.com](https://vercel.com)
2. Import the project from GitHub or upload files
3. Deploy instantly

### Option 4: Custom Server

Upload all files to your web server via FTP/SFTP. Make sure `index.html` is set as the default document.

## 🔗 URLs for App Store

After deploying, use these URLs in your App Store Connect submission:

- **Marketing URL**: `https://yourdomain.com/`
- **Support URL**: `https://yourdomain.com/support-en.html`
- **Privacy Policy URL**: `https://yourdomain.com/privacy-en.html`

The main `index.html` will automatically redirect users to their language version based on browser settings.

## ✏️ Updating Content

To update the content:

1. Edit the respective HTML file(s)
2. Commit and push to GitHub (if using GitHub Pages)
3. Or re-upload to Netlify/Vercel/your server

## 📱 Features

- **Responsive Design**: Works on mobile, tablet, and desktop
- **Auto Language Detection**: Main index.html detects browser language
- **Consistent Styling**: All pages use the same design system
- **Fast Loading**: Minimal CSS, no external dependencies
- **SEO Optimized**: Proper meta tags and semantic HTML

## 🎨 Customization

To customize colors, edit the CSS `background` gradient in the header sections:

```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

To customize fonts, modify the `font-family` in the body style:

```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

## 📧 Support

For questions about the website, contact: inventory.ai.app@gmail.com

---

Made with ❤️ for Inventory.AI
