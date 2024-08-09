import React from 'react'
import Header from "../../components/Header/Header"
import Banner from '../../components/Banner/Banner'
import CategoryBox from '../../components/CategoryBox/CategoryBox'
import DiscountedCarts from '../../components/ِDiscountedCarts/DiscountedCarts'
import PopularCategory from '../../components/PopularCategory/PopularCategory'
import NewProducts from '../../components/NewProducts/NewProducts'
import Mobile from '../../components/Mobiles/Mobile'
import BestSellingProducts from '../../components/BestSellingProducts/BestSellingProducts'
import LapTop from '../../components/LapTops/LapTop'
import Articles from '../../components/Articles/Articles'

export default function Index() {
  return (
    <>
      <Header/>
      <main className='mt-10 px-4 w-full py-4'>
        <Banner/>
        <div className='flex flex-col xl:flex-row mt-20 items-start h-auto xl:h-[25.5rem] justify-between'>
          <DiscountedCarts/>
          <CategoryBox/>
        </div>
        <PopularCategory/>
        <NewProducts />
        <Mobile/>
        <BestSellingProducts/>
        <LapTop/>
        <Articles/>
        <br />
      </main>
    </>
  )
}
