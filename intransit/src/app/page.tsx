"use client";

import { signInWithEmailAndPassword } from "firebase/auth";
import { useRouter } from "next/navigation";
import { useState } from "react";
import { toast } from "sonner";
import { z } from "zod";

import { loginFormSchema, LoginForm } from "@/components/login-form";
import { Card, CardTitle } from "@/components/ui/card";

import { firebaseAuth } from "@/lib/firebase/auth";
import { Program } from "@/lib/info";

export default function Home() {
    const [passwordHiddenState, setPasswordHiddenState] = useState(true);
    const router = useRouter();

    /**
     * Attempt authentication with the provided form values.
     * @param values The form values.
     */
    function submitUserLogin(values: z.infer<typeof loginFormSchema>) {
        signInWithEmailAndPassword(firebaseAuth, values.username, values.password)
            .then((userCredential) => {
                const user = userCredential.user;
                toast(`Successfully logged in as ${user.email}`);
                router.push("/dashboard");
            })
            .catch((error) => {
                const errorCode = error.code;
                const errorMessage = error.message;

                toast(`Error: ${errorCode} - ${errorMessage}`);
            });
    }

    /**
     * Toggle the visibility of the password field.
     * @param event The event.
     */
    function togglePasswordVisibility(event: React.MouseEvent<HTMLButtonElement>): void {
        event.preventDefault();
        setPasswordHiddenState(!passwordHiddenState);
    }

    return (
        <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
            <main className="flex flex-col gap-8 row-start-2 items-center sm:items-start">
                <h1 className="text-4xl font-bold text-center sm:text-left">
                    Welcome to <span>{Program.name}</span>
                </h1>
                <h2 className="text-2xl text-center sm:text-left">{Program.description}</h2>
                <div className="self-center pr-4">
                    <Card className="p-16 space-y-6">
                        <CardTitle className="text-2xl font-bold">Login</CardTitle>
                        <LoginForm
                            submitUserLogin={submitUserLogin}
                            togglePasswordVisibility={togglePasswordVisibility}
                            passwordHiddenState={passwordHiddenState}
                        />
                    </Card>
                </div>
            </main>
        </div>
    );
}
