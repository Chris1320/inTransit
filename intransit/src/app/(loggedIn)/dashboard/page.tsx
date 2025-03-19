"use client";

import { TrendingUp } from "lucide-react";
import { LineChart } from "recharts";
import { Area, AreaChart, CartesianGrid, XAxis, YAxis, Line } from "recharts";

import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { ChartConfig, ChartContainer, ChartTooltip, ChartTooltipContent } from "@/components/ui/chart";

export default function DashboardPage() {
    // TODO: This is a placeholder for the dashboard page.
    const thisYearData = [
        { month: "January", total_income: 186000, total_expense: 80000 },
        { month: "February", total_income: 305000, total_expense: 200000 },
        { month: "March", total_income: 237000, total_expense: 120000 },
        { month: "April", total_income: 73000, total_expense: 190000 },
        { month: "May", total_income: 209000, total_expense: 130000 },
        { month: "June", total_income: 214000, total_expense: 140000 },
    ];

    const chartConfigA = {
        total_income: {
            label: "Total Income",
            color: "hsl(var(--chart-1))",
        },
        total_expense: {
            label: "Total Expense",
            color: "hsl(var(--chart-2))",
        },
    } satisfies ChartConfig;

    const thisWeekData = [
        { week: "1st Week", piattos: 23 },
        { week: "2nd Week", piattos: 14 },
        { week: "3rd Week", piattos: 58 },
        { week: "4th Week", piattos: 58 }
    ];

    const chartConfigB = {
        desktop: {
            label: "Desktop",
            color: "hsl(var(--chart-1))",
        },
    } satisfies ChartConfig;

    return (
        <div>
            <div>
                <Card>
                    <CardHeader>
                        <CardTitle>Last 6 Months</CardTitle>
                        <CardDescription>
                            Showing total income and expenses of schools for the last 6 months
                        </CardDescription>
                    </CardHeader>
                    <CardContent>
                        <ChartContainer config={chartConfigA}>
                            <AreaChart
                                data={thisYearData}
                                margin={{
                                    left: 12,
                                    right: 12,
                                }}
                            >
                                <CartesianGrid vertical={false} />
                                <YAxis
                                    tickLine={false}
                                    axisLine={false}
                                    tickMargin={8}
                                    tickFormatter={(value) => `₱${value / 1000}k`}
                                />
                                <XAxis
                                    dataKey="month"
                                    tickLine={false}
                                    axisLine={false}
                                    tickMargin={8}
                                    tickFormatter={(value) => value.slice(0, 3)}
                                />
                                <ChartTooltip cursor={false} content={<ChartTooltipContent indicator="dot" />} />
                                <Area
                                    dataKey="total_income"
                                    type="natural"
                                    fill="var(--color-total_income)"
                                    fillOpacity={0.4}
                                    stroke="var(--color-total_income)"
                                    stackId="a"
                                />
                                <Area
                                    dataKey="total_expense"
                                    type="natural"
                                    fill="var(--color-total_expense)"
                                    fillOpacity={0.4}
                                    stroke="var(--color-total_expense)"
                                    stackId="a"
                                />
                            </AreaChart>
                        </ChartContainer>
                    </CardContent>
                    <CardFooter>
                        <div className="flex w-full items-start gap-2 text-sm">
                            <div className="grid gap-2">
                                <div className="flex items-center gap-2 font-medium leading-none">
                                    Trending up by 5.2% this month <TrendingUp className="h-4 w-4" />
                                </div>
                                <div className="flex items-center gap-2 leading-none text-muted-foreground">
                                    January - June 2024
                                </div>
                            </div>
                        </div>
                    </CardFooter>
                </Card>
            </div>

            <div>
                <Card>
                    <CardHeader>
                        <CardTitle>Weekly Sales</CardTitle>
                        <CardDescription>This is the Sales Weekly for this Month</CardDescription>
                    </CardHeader>
                    <CardContent>
                        <ChartContainer config={chartConfigB}>
                            <LineChart
                                data={thisWeekData}
                                margin={{
                                    left: 12,
                                    right: 12,
                                }}
                            >
                                <CartesianGrid vertical={false} />
                                <XAxis
                                    dataKey="month"
                                    tickLine={false}
                                    axisLine={false}
                                    tickMargin={8}
                                    tickFormatter={(value) => value.slice(0, 3)}
                                />
                                <ChartTooltip cursor={false} content={<ChartTooltipContent hideLabel />} />
                                <Line
                                    type="natural"
                                    dataKey="piattos"
                                    stroke="var(--color-piattos)"
                                    strokeWidth={2}
                                    dot={false}
                                />
                            </LineChart>
                        </ChartContainer>
                    </CardContent>
                    <CardFooter className="flex-col items-start gap-2 text-sm">
                        <div className="flex gap-2 font-medium leading-none">
                            Trending up by 5.2% this month <TrendingUp className="h-4 w-4" />
                        </div>
                        <div className="leading-none text-muted-foreground">
                            Showing total sales of piattos for the last 3 weeks
                        </div>
                    </CardFooter>
                </Card>
            </div>
        </div>
    );
}
