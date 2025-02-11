"use client";

import { useRouter } from "next/navigation";
import { useEffect } from "react";

export default function LogoutPage() {
    const router = useRouter();
    useEffect(() => {
        localStorage.removeItem("user");
        router.push("/");
    }, [router]);
    return (
        <div>
            <p>You have logged out successfully.</p>
        </div>
    );
}
