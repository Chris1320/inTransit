import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import { Toaster } from "@/components/ui/sonner";
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert";
import { LuCircleAlert } from "react-icons/lu";
import { Program } from "@/lib/info";

import "./globals.css";

const geistSans = Geist({
    variable: "--font-geist-sans",
    subsets: ["latin"],
});

const geistMono = Geist_Mono({
    variable: "--font-geist-mono",
    subsets: ["latin"],
});

export const metadata: Metadata = {
    title: Program.name,
    description: Program.description,
};

export default function RootLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <html lang="en">
            <body className={`${geistSans.variable} ${geistMono.variable} antialiased`}>
                {children}
                <Toaster richColors />
                {process.env.NODE_ENV === "development" && (
                    <div className="fixed top-0 right-0 p-4">
                        <Alert variant="destructive" className="bg-slate-50">
                            <LuCircleAlert className="h-4 w-4" />
                            <AlertTitle>Heads up!</AlertTitle>
                            <AlertDescription>
                                This is a development build and the local environment is used. Set{" "}
                                <code>NODE_ENV=production</code> to use in production.
                            </AlertDescription>
                        </Alert>
                    </div>
                )}
            </body>
        </html>
    );
}
