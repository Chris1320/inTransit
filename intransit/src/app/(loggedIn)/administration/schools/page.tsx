"use client";

import { useEffect, useState } from "react";
import { Table, TableBody, TableCaption, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { Checkbox } from "@/components/ui/checkbox";
import { toast } from "sonner";
import { contactFunction } from "@/lib/firebase";
import { CirclePlus, Edit, Trash } from "lucide-react";
import { Button } from "@/components/ui/button";

export default function SchoolsPage() {
    return (
        <div className="content-center">
            <div>
                <h1 className="text-3xl font-bold">Schools</h1>
                <div className="flex justify-between items-center mt-4">
                    <div className="flex space-x-4">
                        <Button variant="outline">
                            <CirclePlus /> Add User
                        </Button>
                        <input type="text" placeholder="Search Schools" className="input pl-2 " />
                    </div>
                </div>
            </div>
            <Table className="table-hover">
                <TableCaption>Schools</TableCaption>

                <TableHeader>
                    <TableRow>
                        <TableHead className="w-[100px]"></TableHead>
                        <TableHead>School Name</TableHead>
                        <TableHead>Location</TableHead>
                        <TableHead>Actions</TableHead>
                    </TableRow>
                </TableHeader>
                <TableBody>
                    <TableRow>
                        <TableCell>
                            <Checkbox />
                        </TableCell>
                        <TableCell className="font-medium">Baliuag University</TableCell>
                        <TableCell className="font-medium">Baliwag, Bulacan</TableCell>
                        <TableCell className="text-right1">
                            <Button variant="icon">
                                <Edit />
                            </Button>
                            <Button variant="icon">
                                <Trash />
                            </Button>
                        </TableCell>
                    </TableRow>
                </TableBody>
            </Table>
        </div>
    );
}
