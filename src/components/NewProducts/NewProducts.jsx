import React from "react";
import TitleBox from "../TitleBox/TitleBox";
import { Swiper, SwiperSlide } from "swiper/react";
import { Navigation , Autoplay} from "swiper/modules";
import ProductsWithDiscount from "../ProductsWithDiscount/ProductsWithDiscount";
import ProdcutsWithNoDiscount from "../ProductsWithNoDiscounts/ProductsWithNoDiscounts";
import "swiper/css";
import 'swiper/css/navigation';
import SlideButtons from "../SlideButtons/SlideButtons";

export default function NewProducts() {
  return (
    <section>
      <div className="mt-20">
        <TitleBox title={"محصولات جدید"} link={"مشاهده همه"} />
      </div>
      <div className="flex items-center justify-between w-[100%] mx-auto mt-10">
        <Swiper 
        className="p-2" 
        direction="horizontal" 
        loop="true" 
        spaceBetween={35} 
        navigation={{nextEl : ".swiper-button-next",prevEl:".swiper-button-prev"}}
        modules={[Navigation,Autoplay]} 
        autoplay={{delay : 3000}} 
        slidesPerView={1}
        breakpoints={{
          576: {
            slidesPerView: 1,
          },
          768: {
            slidesPerView: 2,
          },
          1024: {
            slidesPerView: 2,
            spaceBetween:20
          },
          1200: {
            slidesPerView: 4,
            spaceBetween:25,
            width:1600
          },
        }}
        >
          <SwiperSlide className="w-[100%]"><ProductsWithDiscount /></SwiperSlide>
          <SwiperSlide className="w-[100%]"><ProdcutsWithNoDiscount /></SwiperSlide>
          <SwiperSlide className="w-[100%]"><ProductsWithDiscount /></SwiperSlide>
          <SwiperSlide className="w-[100%]"><ProdcutsWithNoDiscount /></SwiperSlide>
          <SwiperSlide className="w-[100%]"><ProductsWithDiscount /></SwiperSlide>
          <SwiperSlide className="w-[100%]"><ProdcutsWithNoDiscount /></SwiperSlide>
          <SwiperSlide className="w-[100%]"><ProductsWithDiscount /></SwiperSlide>
          <SwiperSlide className="w-[100%]"><ProductsWithDiscount /></SwiperSlide>
          <SwiperSlide className="w-[100%]"><ProdcutsWithNoDiscount /></SwiperSlide>
          <SlideButtons />
        </Swiper>
      </div>
    </section>
  );
}
