'use client'

import Link from "next/link"

export default function Footer(){
    return (
        <footer className="bg-black w-screen py-12 divide-y-2 divide-gray-300">
            <section className="container grid grid-cols-4 mx-auto">
                <section className="flex flex-col space-y-4 px-8">
                    <h1 className="text-xl font-bold text-white capitalize">features</h1>
                    <Link href="/" className="footer-menu">rooms</Link>
                    <Link href="/" className="footer-menu">pricing</Link>
                    <Link href="/" className="footer-menu">amenities</Link>
                </section>
                <section className="flex flex-col space-y-4 px-8">
                    <h1 className="text-xl font-bold text-white capitalize">support</h1>
                    <Link href="/" className="footer-menu">FAQs</Link>
                    <Link href="/" className="footer-menu">feedback & suggestions</Link>
                    <Link href="/" className="footer-menu">billing support</Link>
                </section>
                <section className="flex flex-col space-y-4 px-8">
                    <h1 className="text-xl font-bold text-white capitalize">company</h1>
                    <Link href="/" className="footer-menu">about us</Link>
                    <Link href="/" className="footer-menu">partners</Link>
                    <Link href="/" className="footer-menu">blog</Link>
                </section>
                <section className="flex flex-col space-y-4 px-8">
                    <h1 className="text-xl font-bold text-white capitalize">contact</h1>
                    <Link href="/" className="text-white font-thin hover:text-blue-500">www.example.com</Link>
                </section>
            </section>
        </footer>
    )
}