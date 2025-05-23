const jwt = require('jsonwebtoken');
const { error } = require('../helpers/logger');

const authMiddleware = (req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];
  
  if (!token) {
    error('No token provided');
    return res.status(401).json({ message: 'Unauthorized' });
  }

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
    next();
  } catch (err) {
    error('Invalid token');
    res.status(401).json({ message: 'Unauthorized' });
  }
};

module.exports = authMiddleware;
