import streamlit as st

def main():
    logoUrl = 'https://www.fanniemae.com/sites/g/files/koqyhd191/files/2020-10/fannie-mae-logo-dark-blue.png'
    st.image(logoUrl, width=300)
    st.title("Buyer's Eligibility Aid")
    st.text("Having trouble getting approved for a mortgage? We have information that can help!")

    # Create a sidebar for navigation
    page = st.sidebar.radio("Select a Page", ("Home", "HUD Information", "Non-Profit Organizations", "Real Estate Portals", "Online Forums and Communities"))

    if page == "Home":
        st.subheader("<-- Read Thru Various Resources")
        # Add content for the home page here
        volunteerImage = "https://www.fanniemae.com/sites/g/files/koqyhd191/files/2022-08/making-difference-image1.jpg"
        st.image(volunteerImage, width=700)

    elif page == "HUD Information":
        st.subheader("U.S. Department of Housing and Urban Development")
        st.text("1. Learn more about what you truly can afford")
        st.markdown("- [Home Economics](https://www.hud.gov/sites/documents/homeeconomics-en.pdf)\n- [Home Buying Programs (per state)](https://www.hud.gov/topics/rental_assistance/local)\n- [HUD-Approved Housing Counseling Agency](https://apps.hud.gov/offices/hsg/sfh/hcc/hcs.cfm)")
        st.text("2. Understand your Rights")
        st.markdown("- [Fair Housing Equal Opportunity for All](https://www.hud.gov/sites/documents/FHEO_Booklet_Eng.pdf)\n- [Real Estate Settlement Procedures Act (RESPA)](https://files.consumerfinance.gov/f/201308_cfpb_respa_narrative-exam-procedures.pdf)\n- [Borrower's Rights](https://www.consumerfinance.gov/know-before-you-owe/)\n- [Predatory Lending](https://www.hud.gov/program_offices/housing/sfh/hcc/OHC_PREDLEND)")
        st.text("3. Searching for Loans")
        st.markdown("- [Shop, Compare, Negotiate](https://www.hud.gov/sites/documents/booklet.pdf)\n- [FHA resources](https://www.hud.gov/buying/loans)\n- [Interest Only Loans](https://www.fdic.gov/consumers/consumer/interest-only/index.html)")
        

    elif page == "Non-Profit Organizations":
        st.subheader("Non-Profit Organizations")
        st.markdown("- [NeighborWorks America](https://nhsmass.org/homeownership-education-counseling/)")
        st.markdown("- [National Foundation for Credit Counseling](https://www.nfcc.org/how-we-help/)")
        # Add content for the Non-Profit Organizations page here

    elif page == "Real Estate Portals":
        st.subheader("Real Estate Portals")
        st.markdown("- [Zillow](https://www.zillow.com/)")
        st.markdown("- [Redfin](https://www.redfin.com/)")
        st.markdown("- [Realtor.com](https://www.realtor.com/)")

    elif page == "Online Forums and Communities":
        st.subheader("Online Forums and Communities")
        st.markdown("- [BiggerPockets](https://www.biggerpockets.com/forums/22)")
        st.markdown("- [Reddit](https://www.reddit.com/r/RealEstate/)")
        st.markdown("- [The Mortgage Broker Club](https://themortgagebrokerclub.co.uk/broker-tools/forum-and-adviser-community/)")


if __name__ == "__main__":
    main()
