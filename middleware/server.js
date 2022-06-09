// required libraries
const express = require('express');
const cors = require('cors')
const multer = require('multer');
const { append } = require('express/lib/response');

const app = express()

// cors package for express middleware
app.use(cors())

// multer package serves as a middleware, so the data which is uploaded is stored in the created public folder
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, "public")
    },
    filename: (req, file, cb) => {
        // returns the name of the file
        cb(null, Date.now() + '-' + file.originalname)
    }
});

// only single file upload is needed in the scope of this project
const upload = multer({storage}).single('file');


// post method
app.post('/upload', (req, res) => {
    upload(req, res, (err) => {
        if (err) {
            return res.status(500).json(err)
        }

        return res.status(200).send(req.file)
    })
});

app.listen(8000, () => {
    console.log('Application is running on port 8000.')
});