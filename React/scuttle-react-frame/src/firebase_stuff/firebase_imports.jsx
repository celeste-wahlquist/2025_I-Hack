// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
export const firebaseConfig = {
  apiKey: "AIzaSyA0pxE151QiESUkfhxCFe0OTiDJ4AgrhN0",
  authDomain: "scuttle-521fa.firebaseapp.com",
  projectId: "scuttle-521fa",
  storageBucket: "scuttle-521fa.firebasestorage.app",
  messagingSenderId: "508417060037",
  appId: "1:508417060037:web:34ca5d0a2c3c2a21a214ac",
  measurementId: "G-EGSFJN1D1L"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);