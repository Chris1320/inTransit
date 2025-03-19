import React, { createContext, useState, useContext, useEffect, ReactNode } from "react";
import { Authentication } from "@/lib/info";

interface AuthContextType {
    is_authenticated: boolean; // Whether the user is authenticated
    login: () => void; // Function to log the user in
    logout: () => void; // Function to log the user out
}
interface AuthProviderProps {
    children: ReactNode;
}
const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }): React.FC<AuthProviderProps> {
    const [timeout_id, setTimeoutId] = useState<ReturnType<typeof setTimeout> | null>(null);
    const [is_authenticated, setIsAuthenticated] = useState<boolean>(() => {
        const stored_auth_state = localStorage.getItem("isAuthenticated");
        return stored_auth_state === "true";
    });

    /// Log the user in
    function login() {
        setIsAuthenticated(true);
        localStorage.setItem(Authentication.ls_uia_name, "true");
        startLogoutTimer();
    }

    /// Log the user out
    function logout() {
        setIsAuthenticated(false);
        localStorage.removeItem(Authentication.ls_uia_name);
        if (timeout_id) {
            clearTimeout(timeout_id);
        }
    }

    /// Start the logout timer
    function startLogoutTimer() {
        if (timeout_id) {
            clearTimeout(timeout_id);
        }
        const newTimeoutId = setTimeout(() => {
            logout();
            alert("You have been logged out due to inactivity.");
        }, Authentication.default_timeout);
        setTimeoutId(newTimeoutId);
    }

    /// Set up the logout timer when the user is authenticated
    useEffect(() => {
        if (is_authenticated) {
            startLogoutTimer();
        }

        return () => {
            if (timeout_id) {
                clearTimeout(timeout_id);
            }
        };
    }, [is_authenticated]);

    return <AuthContext.Provider value={{ is_authenticated, login, logout }}>{children}</AuthContext.Provider>;
}

/// Hook to access the authentication context.
// This hook is used to access the authentication context in a component
export function useAuth(): AuthContextType {
    const ctx = useContext(AuthContext);
    if (!ctx) {
        throw new Error("useAuth must be used within an AuthProvider");
    }
    return ctx;
}
