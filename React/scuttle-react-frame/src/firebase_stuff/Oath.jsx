// add the auth variable and a few auth-related functions from firebase (NOT LOCAL FIREBASE)
import { auth } from "./firebase_imports";
import {  GoogleAuthProvider, signInWithPopup, signOut } from "firebase/auth";

    // declare a new google provider variable
    const googleProvider = new GoogleAuthProvider();

    
    // export the sign in function
    export const handleGoogleSignIn = async () => {
        // try and catch statements ensure authentication is present
        try {
            // calls the popUp function, passes provider and user
            await signInWithPopup(auth, googleProvider);
            alert("Google Sign-In Success!");
        } catch (error) {
            handleAuthError(error);
        }
    }; 

    // export the log out function
    export const handleLogout = async () => {
        // try and catch statements ensure the function is correctly called
        // (not exactly sure how an error could come up, but just in case)
        try {
            // waits to see if the user is passed through the signout function
            await signOut(auth);
            alert("Logged out!");
        } catch (error) {
            handleAuthError(error);
        }
    };

    // error handler, called in both the log in/log out functions
    const handleAuthError = (error) => {
        // error is the parameter, it's a unique variable type
        // lets the user know and error occured
        let message = "An error occurred. Please try again.";
        // access the specific code from the error item, and describes what the code means
        if (error.code === "auth/email-already-in-use") {
            message = "This email is already in use. Try logging in.";
        } else if (error.code === "auth/invalid-email") {
            message = "Invalid email format.";
        } else if (error.code === "auth/weak-password") {
            message = "Password should be at least 6 characters.";
        } else if (error.code === "auth/wrong-password") {
            message = "Incorrect password. Try again.";
        }
        // pass the message as an alert
        alert(message);
    };