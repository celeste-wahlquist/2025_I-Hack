import { doc, setDoc, getDoc, getFirestore } from "firebase/firestore";
import { initializeApp } from "firebase/app";
import {firebaseConfig} from "./firebase_imports"
// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Firestore and export
export const db = getFirestore(app);

export async function createUser(userId, username, ingredients, shoppingList, recipes) {
  await setDoc(doc(db, "users", userId), {
    username: username,
    possessedIngredients: ingredients,
    shoppingList: shoppingList,
    desiredRecipes: recipes
  });
  console.log("User created/updated successfully!");
}

// import { getDoc, doc } from "firebase/firestore";

export async function getUser(userId) {
  const docRef = doc(db, "users", userId);
  const docSnap = await getDoc(docRef);

  if (docSnap.exists()) {
    console.log("User data:", docSnap.data());
  } else {
    console.log("No such user!");
  }
}

// Example usage:
// createUser("user123", "JohnDoe", ["eggs", "milk"]);
// export default Data