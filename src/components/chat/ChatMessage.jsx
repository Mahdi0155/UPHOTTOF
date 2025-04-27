import React from 'react';

const ChatMessage = ({ message, sender }) => {
  return (
    <div className={`chat-message ${sender === 'user' ? 'user' : 'bot'}`}>
      <div className="message-content">{message}</div>
    </div>
  );
};

export default ChatMessage;
