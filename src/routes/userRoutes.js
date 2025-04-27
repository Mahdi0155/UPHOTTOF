const express = require('express');
const router = express.Router();
const userController = require('../controllers/userController');

router.post('/start', userController.start);
router.post('/help', userController.help);
router.post('/settings', userController.settings);

module.exports = router;
