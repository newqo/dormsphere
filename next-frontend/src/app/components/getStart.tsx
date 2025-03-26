'use client'

import Link from "next/link";

export default function GetStart(){
    return (
        <section className="bg-[url(/images/room2.jpg)] bg-no-repeat bg-cover bg-center w-full h-200">
            <section className="inset-0 bg-black/50 w-full h-200 flex flex-col justify-center items-center mx-auto px-20 space-y-4">
                <h1 className="font-bold text-9xl text-white drop-shadow-2xl text-center">dormsphere.</h1>
                <p className="text-white text-center text-lg px-32">Welcome to DormSphere, where modern living meets student convenience. Designed for those who seek a balanced lifestyle, DormSphere offers a space that perfectly blends comfort, security, and community.</p>
                <Link href="/viewmore" className="view-btn mt-4 cursor-pointer">view more</Link>
            </section>
        </section>
    );
}