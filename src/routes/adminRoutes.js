const express = require('express');
const router = express.Router();
const adminController = require('../controllers/adminController');
const authMiddleware = require('../middlewares/authMiddleware');

router.use(authMiddleware.isAdmin);

router.post('/send-broadcast', adminController.sendBroadcast);
router.get('/users', adminController.getAllUsers);

module.exports = router;
