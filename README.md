# Stock Graph Analyzer Edge Extension

This extension allows you to capture a screenshot of the current tab (e.g., a stock chart), send it to an LLM backend for technical analysis, and receive buy/sell/hold advice.

## Features
- Capture visible tab as an image
- Send image to backend API for LLM analysis (integration required)
- Display analysis in popup

## Usage
1. Load the extension in Edge (edge://extensions > Load unpacked)
2. Click the extension icon and use the popup to capture and analyze the current page

## Setup
- Add your backend API endpoint in `popup.js` where indicated.
- Add your own icons (icon16.png, icon48.png, icon128.png) in the root directory.

## Note
This is a starter template. Backend API and icons must be provided by you.
