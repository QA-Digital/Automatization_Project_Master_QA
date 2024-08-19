const express = require('express');
const path = require('path');
const cors = require('cors');

const app = express();
app.use(cors());  // Enable CORS to allow requests from your Flask app

// Endpoint to serve the file
app.get('/download', (req, res) => {
    const filePath = path.resolve('C:/Users/KDK/Desktop/DTCZ/kod/Automatization_Project_Master_QA/app/report/script.js');
    res.download(filePath, 'script.js', (err) => {
        if (err) {
            console.error('Error during file download:', err);
            res.status(500).send('Error during file download');
        }
    });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Express server running on port ${PORT}`);
});
