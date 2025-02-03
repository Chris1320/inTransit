import { getAuth } from "firebase/auth";
import { firebaseApp } from "@/lib/firebase/firebase";

export const firebaseAuth = getAuth(firebaseApp);
