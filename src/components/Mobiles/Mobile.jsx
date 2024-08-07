import React from 'react'
import TitleBox from '../TitleBox/TitleBox'
import ProductsWithDiscount from '../ProductsWithDiscount/ProductsWithDiscount'
import ProductsWithNoDiscounts from '../ProductsWithNoDiscounts/ProductsWithNoDiscounts'
import {Swiper,SwiperSlide} from "swiper/react";
import { Autoplay } from 'swiper/modules';

export default function Mobile() {
  return (
    <section className='mt-20'>
      <TitleBox title={"موبایل ها"} link={"مشاهده همه"} />
      <div className='flex items-center mt-10 justify-between w-[100%] h-full'>
       <div className='w-[20%] h-[30rem] rounded-3xl overflow-hidden shadow-2xl'>
         <div className='w-[100%] h-[100%]'>
            <img src="public/images/mobile/Mobile.jpg" className='w-[100%] h-[100%]' alt="" />
         </div>
       </div>
       <div className='w-[75%] mx-auto flex items-center justify-between'>
           <Swiper
            className='p-5'
            modules={[Autoplay]}
            slidesPerView={3}
            spaceBetween={30}
            loop="true"
            autoplay={{
                delay:3000
            }}
           >
             <SwiperSlide><ProductsWithDiscount/></SwiperSlide>
             <SwiperSlide><ProductsWithNoDiscounts/></SwiperSlide>
             <SwiperSlide><ProductsWithDiscount/></SwiperSlide>
             <SwiperSlide><ProductsWithNoDiscounts/></SwiperSlide>
             <SwiperSlide><ProductsWithDiscount/></SwiperSlide>
           </Swiper>
       </div>
      </div>
    </section>
  )
}
