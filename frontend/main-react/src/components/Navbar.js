import React from 'react'
import '../css/Navbar.css'
import Logo from '../img/JC-white.svg'

export default function Navbar() {
    return (
        <div className='desktop-navbar'>
            <div className="logo"> <img src={Logo} alt="no img"/></div>
            <ul>
                <li>Home</li>
                <li>Courses</li>
                <li>Portofolios</li>
                <li>Contact</li>
            </ul>
            <div className="user"> Eduard Boghian</div>
        </div>
    )
}


