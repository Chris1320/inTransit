import { initializeApp } from "firebase/app";

import { firebaseConfig } from "@/lib/firebase/_config";
// https://firebase.google.com/docs/web/setup#available-libraries

export const firebaseApp = initializeApp(firebaseConfig);
