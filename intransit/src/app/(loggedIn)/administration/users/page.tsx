"use client";

import { useEffect, useState } from "react";
import { Table, TableBody, TableCaption, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { Checkbox } from "@/components/ui/checkbox";
import { toast } from "sonner";
import { contactFunction } from "@/lib/firebase";
import { CirclePlus, Edit, Trash } from "lucide-react";
import { Button } from "@/components/ui/button";

export default function UsersPage() {
    const [users, setUsers] = useState([]);
    useEffect(() => {
        const fetchData = async () => {
            try {
                const result = await contactFunction("get_all_users", { method: "GET" });
                setUsers(await result.json());
            } catch (error) {
                console.error(error);
                toast.error("There was an error getting the list of users. Please try again later.");
            }
        };

        fetchData();
    }, []);

    return (
        <div className="content-center">
            <div>
                <h1 className="text-3xl font-bold">Users</h1>
                <div className="flex justify-between items-center mt-4">
                    <div className="flex space-x-4">
                        <Button variant="outline">
                            <CirclePlus /> Add User
                        </Button>
                        <input type="text" placeholder="Search Users" className="input pl-2 " />
                    </div>
                </div>
            </div>
            <Table className="table-hover">
                <TableCaption>Users</TableCaption>

                <TableHeader>
                    <TableRow>
                        <TableHead className="w-[100px]"></TableHead>
                        <TableHead>Employee I.D.</TableHead>
                        <TableHead>First Name</TableHead>
                        <TableHead>Middle Name</TableHead>
                        <TableHead>Last Name</TableHead>
                        <TableHead>Email</TableHead>
                        <TableHead>User Level</TableHead>
                        <TableHead>Department</TableHead> {/* New column */}
                        <TableHead>Actions</TableHead>
                    </TableRow>
                </TableHeader>
                <TableBody>
                    {users.map((user) => (
                        <TableRow key={user.uid}>
                            <TableCell>
                                <Checkbox />
                            </TableCell>
                            <TableCell className="font-medium">{user.uid}</TableCell>
                            <TableCell className="font-medium">N/A</TableCell>
                            <TableCell className="font-medium">N/A</TableCell>
                            <TableCell className="font-medium">N/A</TableCell>
                            <TableCell>{user.email}</TableCell>
                            <TableCell>{user.user_level}</TableCell>
                            <TableCell>{user.department}</TableCell> {/* New cell */}
                            <TableCell className="text-right1">
                                <Button variant="icon">
                                    <Edit />
                                </Button>
                                <Button variant="icon">
                                    <Trash />
                                </Button>
                            </TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </div>
    );
}
