document.getElementById('captureBtn').addEventListener('click', async () => {
  document.getElementById('result').innerText = 'Capturing...';
  try {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    chrome.tabs.captureVisibleTab(tab.windowId, { format: 'png' }, (dataUrl) => {
      if (chrome.runtime.lastError) {
        document.getElementById('result').innerText = 'Error: ' + chrome.runtime.lastError.message;
        return;
      }
      document.getElementById('result').innerHTML = '<img src="' + dataUrl + '" style="max-width:100%"><br>Sending to LLM...';
      // Send dataUrl to backend API for LLM analysis
      fetch('https://your-backend-api/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ image: dataUrl })
      })
      .then(res => res.json())
      .then(data => {
        document.getElementById('result').innerText = data.analysis;
      })
      .catch(err => {
        document.getElementById('result').innerText = 'API Error: ' + err.message;
      });
    });
  } catch (e) {
    document.getElementById('result').innerText = 'Error: ' + e.message;
  }
});
