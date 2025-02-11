"use client";

import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import { toast } from "sonner";
import { z } from "zod";

import { SignUpForm, SignUpFormSchema } from "@/components/signup-form";
import { Card, CardTitle } from "@/components/ui/card";

import { Program } from "@/lib/info";
import { contactFunction } from "@/lib/firebase";

export default function Page() {
    const [passwordHiddenState, setPasswordHiddenState] = useState(true);
    const router = useRouter();

    useEffect(() => {
        const fetchData = async () => {
            try {
                const result = await (await contactFunction("first_run", { method: "GET" })).json();
                if (!result) {
                    router.push("/");
                }
            } catch (error) {
                console.error(error);
            }
        };

        fetchData();
    }, [router]);

    /**
     * Attempt authentication with the provided form values.
     * @param values The form values.
     */
    async function submitUserSignUp(values: z.infer<typeof SignUpFormSchema>) {
        if (values.password !== values.passwordConfirm) {
            toast.error("Passwords do not match");
            return;
        }

        try {
            const data = {
                creator_uid: null,
                display_name: values.displayname,
                email: values.username,
                password: values.password,
                user_level: null,
            };
            const response = await contactFunction("user_register", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
            });

            if (response.ok) {
                toast.success("Successfully registered");
                router.push("/");
            } else {
                toast.error(`Error registering user: ${await response.text()}`);
            }
        } catch (error) {
            console.error(error);
        }
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
            <main className="flex flex-col gap-4 row-start-2 items-center sm:items-start">
                <h1 className="text-4xl font-bold text-center sm:text-left">
                    Welcome to <span>{Program.name}</span>
                </h1>
                <h2 className="text-2xl text-center sm:text-left">{Program.description}</h2>
                <p>Please create a new superintendent account.</p>
                <div className="self-center pr-4">
                    <Card className="p-16 space-y-5">
                        <CardTitle className="text-2xl font-bold">Register</CardTitle>
                        <SignUpForm
                            submitUserSignUp={submitUserSignUp}
                            togglePasswordVisibility={togglePasswordVisibility}
                            passwordHiddenState={passwordHiddenState}
                        />
                    </Card>
                </div>
            </main>
        </div>
    );
}
