"use client";

import { Home, Settings, UsersIcon, School, ChartArea, LogOut } from "lucide-react";

import {
    Sidebar,
    SidebarContent,
    SidebarFooter,
    SidebarGroup,
    SidebarHeader,
    SidebarGroupLabel,
    SidebarGroupContent,
    SidebarMenu,
    SidebarMenuItem,
    SidebarMenuButton,
} from "@/components/ui/sidebar";
import { Program } from "@/lib/info";

export function AppSidebar() {
    const sidebar_items = [
        {
            category: "",
            items: [
                { title: "Dashboard", url: "/dashboard", icon: Home },
                { title: "Reports", url: "/reports", icon: ChartArea },
            ],
        },
        {
            category: "Administration",
            items: [
                {
                    title: "Schools",
                    url: "/administration/schools",
                    icon: School,
                },
                {
                    title: "Users",
                    url: "/administration/users",
                    icon: UsersIcon,
                },
                {
                    title: "Server Settings",
                    url: "/administration/settings",
                    icon: Settings,
                },
            ],
        },
        {
            category: "Account",
            items: [
                {
                    title: "Profile",
                    url: "/account/profile",
                    icon: UsersIcon,
                },
                {
                    title: "Settings",
                    url: "/account/settings",
                    icon: Settings,
                },
                {
                    title: "Logout",
                    url: "/logout",
                    icon: LogOut,
                },
            ],
        },
    ];

    return (
        <Sidebar>
            <SidebarHeader>{Program.name}</SidebarHeader>
            <SidebarContent>
                {sidebar_items.map((item) => (
                    <SidebarGroup key={item.category}>
                        <SidebarGroupLabel>{item.category}</SidebarGroupLabel>
                        <SidebarGroupContent>
                            <SidebarMenu>
                                {item.items.map((item) => (
                                    <SidebarMenuItem key={item.title}>
                                        <SidebarMenuButton asChild>
                                            <a href={item.url}>
                                                <item.icon />
                                                <span>{item.title}</span>
                                            </a>
                                        </SidebarMenuButton>
                                    </SidebarMenuItem>
                                ))}
                            </SidebarMenu>
                        </SidebarGroupContent>
                    </SidebarGroup>
                ))}
            </SidebarContent>
            <SidebarFooter />
        </Sidebar>
    );
}
