@looking_products
Feature: Search products

   Feature I as a user want to search for products

   Background: Acess base page
     Given I acess base page

   @looking_books
   Scenario: Go to the books page
      When I press the books button
      Then I see books page