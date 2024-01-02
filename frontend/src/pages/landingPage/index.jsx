import TopBar from "./topBar";
import HeroSection from "./heroSection";
import AboutUsSection from "./aboutUsSection";
import ServicesSection from "./servicesSection";
import WhyUsSection from "./whyUsSection";

function LandingPage(props) {
  return <div className='body body-landingpage'>
    <TopBar />
    <HeroSection />
    <AboutUsSection />
    <ServicesSection />
    <WhyUsSection />
  </div>
}

export default LandingPage;