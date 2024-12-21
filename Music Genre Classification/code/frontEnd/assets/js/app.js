// Handle file selection
document.getElementById('audioInput').addEventListener('change', (event) => {
    const fileDetailsDiv = document.getElementById('fileDetails');
    const file = event.target.files[0];

    if (file) {
        // Display file details
        fileDetailsDiv.innerHTML = `
            <p><strong>File Name:</strong> ${file.name}</p>
            <p><strong>File Size:</strong> ${(file.size / 1024).toFixed(2)} KB</p>
            <p><strong>File Type:</strong> ${file.type}</p>
        `;
    } else {
        // Reset if no file is selected
        fileDetailsDiv.innerHTML = '<p>No file selected.</p>';
    }
});

// Handle the "Classify Genre" button click
document.getElementById('classifyButton').addEventListener('click', () => {
    const resultsDiv = document.getElementById('results');
    const file = document.getElementById('audioInput').files[0];

    if (!file) {
        resultsDiv.innerText = 'Please upload an audio file before classifying.';
        return;
    }

    // Simulating classification result (replace this with real API calls)
    resultsDiv.innerText = 'Processing your file...';
    setTimeout(() => {
        const mockResponse = {
            genre: 'Rock',
            confidence: '85%',
        };
        resultsDiv.innerText = 
            `Predicted Genre: ${mockResponse.genre} (Confidence: ${mockResponse.confidence})`;
    }, 2000);
});
