import { zodResolver } from "@hookform/resolvers/zod";
import { Eye, EyeClosed } from "lucide-react";
import { useForm } from "react-hook-form";
import { z } from "zod";

import { FormLabel, FormItem, FormField, FormControl, FormMessage } from "@/components/ui/form";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Form } from "@/components/ui/form";

import { cn } from "@/lib/utils";

export const SignUpFormSchema = z.object({
    displayname: z.string(),
    username: z.string(),
    password: z.string(),
    passwordConfirm: z.string(),
});

interface SignUpFormProps {
    submitUserSignUp: (values: z.infer<typeof SignUpFormSchema>) => void;
    togglePasswordVisibility: (event: React.MouseEvent<HTMLButtonElement>) => void;
    passwordHiddenState: boolean;
    className?: string;
}

export function SignUpForm({
    submitUserSignUp,
    togglePasswordVisibility,
    passwordHiddenState,
    className,
}: SignUpFormProps) {
    const form = useForm<z.infer<typeof SignUpFormSchema>>({
        resolver: zodResolver(SignUpFormSchema),
        defaultValues: {
            displayname: "",
            username: "",
            password: "",
            passwordConfirm: "",
        },
    });

    return (
        <div className={cn("w-full max-w-sm", className)}>
            <Form {...form}>
                <form onSubmit={form.handleSubmit(submitUserSignUp)} className="space-y-5">
                    <div className="flex justify-between space-x-2">
                        <FormField
                            control={form.control}
                            name="displayname"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>Full Name</FormLabel>
                                    <FormControl>
                                        <Input id="form-login-displayname" type="text" required {...field} />
                                    </FormControl>
                                    {/* <FormDescription></FormDescription> */}
                                    <FormMessage />
                                </FormItem>
                            )}
                        />
                    </div>
                    <div className="flex justify-between space-x-2">
                        <FormField
                            control={form.control}
                            name="username"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>Email</FormLabel>
                                    <FormControl>
                                        <Input id="form-login-username" type="email" required {...field} />
                                    </FormControl>
                                    {/* <FormDescription></FormDescription> */}
                                    <FormMessage />
                                </FormItem>
                            )}
                        />
                    </div>
                    <div className="flex justify-between space-x-2">
                        <FormField
                            control={form.control}
                            name="password"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>Password</FormLabel>
                                    <FormControl>
                                        <Input type={passwordHiddenState ? "password" : "text"} required {...field} />
                                    </FormControl>
                                    {/* <FormDescription></FormDescription> */}
                                    <FormMessage />
                                </FormItem>
                            )}
                        />
                        {/* TODO: Fix button position */}
                        <Button type="button" onClick={togglePasswordVisibility}>
                            {passwordHiddenState ? <Eye /> : <EyeClosed />}
                        </Button>
                    </div>
                    <div className="flex justify-between space-x-2">
                        <FormField
                            control={form.control}
                            name="passwordConfirm"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>Repeat Password</FormLabel>
                                    <FormControl>
                                        <Input type={passwordHiddenState ? "password" : "text"} required {...field} />
                                    </FormControl>
                                    {/* <FormDescription></FormDescription> */}
                                    <FormMessage />
                                </FormItem>
                            )}
                        />
                    </div>
                    <Button type="submit">Submit</Button>
                </form>
            </Form>
        </div>
    );
}
