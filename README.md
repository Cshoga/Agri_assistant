# Agri_assistant

Overview

Agri_assistant is a web-based chatbot interface designed to assist users with agricultural-related queries in english, such as information about crops, soil, weather, and farming practices. This chatbot interacts with users and provides responses fetched from a backend API.

Features

- Interactive Chat Interface: Users can send messages and receive responses from the chatbot.
- System Messages: Initial guidance message for users.
- API Integration: Communicates with a backend API for fetching and sending messages.
- Chat Clearing: Allows users to reset the chat conversation.
- Loading Indicator: Shows a loading spinner when fetching a response.
- User-friendly Design: Simple and intuitive UI built with Next.js and Tailwind CSS.
  
# Installation

## Prerequisites

Ensure you have the following installed on your system:

- Node.js (>= 14.x recommended)

## Steps to Run Locally

- Clone the repository: git clone https://github.com/Cshoga/Agri_assistant.git

## Install dependencies:

- npm install

## Start the development server:

- npm run dev
- Ensure the backend API is running at http://localhost:8080/api/home/.
- Open http://localhost:3000 in your browser.

## Usage

Start the application.

Type a question related to agriculture in the input box.
Click the Send button or press Enter to submit the query.
Wait for the chatbot's response.
Click Clear Chat to reset the conversation.

## API Integration

This chatbot sends user queries to a backend API:

Endpoint: http://localhost:8080/api/home/

Method: POST

Request Body: { "data": "user input here" }

Response: JSON containing the chatbot's reply.

## Technologies Used

- Next.js for the frontend
- Tailwind CSS for styling
- Lucide Icons for UI elements
- Fetch API for data retrieval
