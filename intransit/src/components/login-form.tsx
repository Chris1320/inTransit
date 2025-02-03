import { zodResolver } from "@hookform/resolvers/zod";
import { Eye, EyeClosed } from "lucide-react";
import { useForm } from "react-hook-form";
import { z } from "zod";

import { FormItem, FormField, FormControl, FormMessage } from "@/components/ui/form";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Form } from "@/components/ui/form";

import { cn } from "@/lib/utils";

export const loginFormSchema = z.object({
    username: z.string(),
    password: z.string(),
});

interface LoginFormProps {
    submitUserLogin: (values: z.infer<typeof loginFormSchema>) => void;
    togglePasswordVisibility: (event: React.MouseEvent<HTMLButtonElement>) => void;
    passwordHiddenState: boolean;
    className?: string;
}

export function LoginForm({
    submitUserLogin,
    togglePasswordVisibility,
    passwordHiddenState,
    className,
}: LoginFormProps) {
    const form = useForm<z.infer<typeof loginFormSchema>>({
        resolver: zodResolver(loginFormSchema),
        defaultValues: {
            username: "",
            password: "",
        },
    });

    return (
        <div className={cn("w-full max-w-sm", className)}>
            <Form {...form}>
                <form onSubmit={form.handleSubmit(submitUserLogin)} className="space-y-5">
                    <FormField
                        control={form.control}
                        name="username"
                        render={({ field }) => (
                            <FormItem>
                                {/* <FormLabel>Username</FormLabel> */}
                                <FormControl>
                                    <Input
                                        id="form-login-username"
                                        type="text"
                                        placeholder="Username"
                                        required
                                        {...field}
                                    />
                                </FormControl>
                                {/* <FormDescription></FormDescription> */}
                                <FormMessage />
                            </FormItem>
                        )}
                    />
                    {/* TODO: Adjust alignment */}
                    <div className="flex justify-between space-x-2">
                        <FormField
                            control={form.control}
                            name="password"
                            render={({ field }) => (
                                <FormItem>
                                    {/* <FormLabel>Password</FormLabel> */}
                                    <FormControl>
                                        <Input
                                            type={passwordHiddenState ? "password" : "text"}
                                            placeholder="Password"
                                            required
                                            {...field}
                                        />
                                    </FormControl>
                                    {/* <FormDescription></FormDescription> */}
                                    <FormMessage />
                                </FormItem>
                            )}
                        />
                        <Button onClick={togglePasswordVisibility}>
                            {passwordHiddenState ? <Eye /> : <EyeClosed />}
                        </Button>
                    </div>
                    <Button type="submit">Submit</Button>
                </form>
            </Form>
        </div>
    );
}
