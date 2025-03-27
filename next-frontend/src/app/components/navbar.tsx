import Link from "next/link";

export default function Navbar(){
    return (
        <nav className="bg-white flex top-0 z-10 fixed w-full py-4 shadow">
            <section className="container flex justify-between items-center mx-auto">
                <section className="flex flex-row gap-10 items-center">
                    <Link href="/" id="nav-logo" className="font-bold text-2xl cursor-pointer">dormsphere.</Link>
                    <Link href="/" id="nav-feature" className="nav-menu">features <i className="fa-regular fa-chevron-right font-thin translate-y-0.5"></i></Link>
                    <Link href="/" id="nav-pricing" className="nav-menu">pricing</Link>
                    <Link href="/" id="nav-amentities" className="nav-menu">amenities</Link>
                </section>
                <section className="flex flex-row items-center justify-center">
                    <Link href="/signin" className="nav-menu">
                        <i className="fa-regular fa-user text-xl translate-y-0.5"></i>
                    </Link>
                </section>
            </section>
        </nav>
    );
}