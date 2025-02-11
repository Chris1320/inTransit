import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar";
import { AppSidebar } from "@/components/app-sidebar";

export default function Layout({ children }: { children: React.ReactNode }) {
    return (
        <SidebarProvider>
            <AppSidebar />
            {/* consume all space */}
            <SidebarTrigger />
            <main className="flex flex-col flex-1 m-24">{children}</main>
        </SidebarProvider>
    );
}
