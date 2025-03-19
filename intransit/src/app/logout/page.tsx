"use client";

import { useRouter } from "next/navigation";
import { useEffect } from "react";
import { useAuth } from "@/lib/authentication";

export default function LogoutPage() {
    const { logout } = useAuth();
    const router = useRouter();
    useEffect(() => {
        logout();
        router.push("/");
    }, [router]);
    return (
        <div>
            <p>You have logged out successfully.</p>
        </div>
    );
}
