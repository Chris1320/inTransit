"use client";

import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar";
import { AppSidebar } from "@/components/app-sidebar";
import { useAuth } from "@/lib/authentication";
import { useRouter } from "next/navigation";
import { useEffect } from "react";

export default function Layout({ children }: { children: React.ReactNode }) {
    const { is_authenticated } = useAuth();
    const router = useRouter();

    useEffect(() => {
        if (!is_authenticated) {
            router.push("/"); // Redirect to the login page if not authenticated
        }
    }, [is_authenticated, router]);

    if (!is_authenticated) {
        return null; // Optionally, render nothing while redirecting
    }

    return (
        <SidebarProvider>
            <AppSidebar />
            <SidebarTrigger />
            <main className="flex flex-col flex-1 m-24">{children}</main>
        </SidebarProvider>
    );
}
