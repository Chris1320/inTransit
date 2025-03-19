// https://firebase.google.com/docs/web/setup#available-libraries
import { initializeApp, getApps, getApp } from "firebase/app";
import { connectAuthEmulator, getAuth } from "firebase/auth";
import { getFirestore, connectFirestoreEmulator } from "firebase/firestore";

const firebaseConfig = {
    apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
    authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
    projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
    storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
    messagingSenderId: process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID,
    appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID,
};

const app = !getApps().length ? initializeApp(firebaseConfig) : getApp();
const auth = getAuth(app);
const fstore = getFirestore(app);
let functions_endpoint = new URL(
    `https://us-central1-${process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID}.cloudfunctions.net`
);

if (process.env.NODE_ENV === "development") {
    // TODO: Read `firebase.json` for emulator settings.
    // const firebase_config = await fs.readFile("firebase.json", "utf-8");
    // const { emulators } = JSON.parse(firebase_config);
    // if (emulators) {
    //     connectAuthEmulator(auth, `http://localhost:${emulators.auth.port}`);
    //     functions_endpoint = new URL(`http://localhost:${emulators.functions.port}/deped-intransit/us-central1/`);
    // }

    connectAuthEmulator(auth, "http://localhost:9099", { disableWarnings: true });
    connectFirestoreEmulator(fstore, "localhost", 8080);
    functions_endpoint = new URL(`http://localhost:5001/deped-intransit/us-central1/`);
}

/**
 * Contact a Firebase Function.
 * @param endpoint The endpoint.
 * @param data The data.
 */
async function contactFunction(endpoint: string, data?: object): Promise<Response> {
    return await fetch(new URL(endpoint, functions_endpoint), data);
}

export { app, auth, fstore, contactFunction };
