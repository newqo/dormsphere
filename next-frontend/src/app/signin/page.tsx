'use client'

import Link from "next/link";

export default function Page(){
    return (
        <section className="bg-[url(/images/room1.jpg)] bg-no-repeat bg-cover bg-center w-full h-200">
            <section className="inset-0 bg-black/50 w-full h-200">
                <section className="container mx-auto flex flex-col justify-center px-4 py-20 items-center">
                    <section className="container mx-auto p-20 w-1/2 border border-gray-100 shadow-xl rounded-3xl bg-white flex flex-col items-center space-y-12">
                        <h1 className="text-5xl font-bold capitalize">sign in</h1>
                        <form action="" className="space-y-4 w-full">
                            <section className="flex flex-col space-y-2 items-start w-full">
                                <label htmlFor="input-email" className="capitalize font-bold">email</label>
                                <input type="email" 
                                name="input-email" id="input-email"
                                placeholder="Enter your email"
                                required
                                className="border border-gray-400 px-4 py-2 focus:ring-1 focus:outline-none rounded-full w-full"/>
                            </section>
                            <section className="flex flex-col space-y-2 items-start">
                                <label htmlFor="input-password" className="capitalize font-bold">password</label>
                                <input type="password" 
                                name="input-password" id="input-password"
                                placeholder="Enter your password"
                                required
                                className="border border-gray-400 px-4 py-2 focus:ring-1 focus:outline-none rounded-full w-full"/>
                            </section>
                            <section className="flex flex-col space-x-4 justify-center items-center py-2">
                                <button type="submit" className="submit-btn">sign in</button>
                                <section className="flex flex-row gap-2 py-2">
                                    <p className="text-sm font-thin">Don't have an account yet?</p>
                                    <Link href="/signup" className="text-sm font-bold text-blue-500 underline">sign up</Link>
                                </section>
                            </section>
                        </form>
                    </section>
                </section>
            </section>
        </section>
    );
}