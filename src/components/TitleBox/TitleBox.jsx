import React from 'react'
import { Link } from 'react-router-dom'

export default function TitleBox({title,link}) {
  return (
    <div className='flex mt-10 items-center justify-between'>
       <p className='font-YekanBakh font-bold text-secondary text-[1.1rem] md:text-[1.5rem]'>{title}</p>
       <Link className='font-YekanBakh font-bold text-secondary text-[0.9rem] md:text-[1.1rem]' to={"#"}>{link}</Link>
    </div>
  )
}
