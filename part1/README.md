HBnB - Part 1: Technical Documentation

This project is the first phase of the HBnB Evolution application, which aims to simulate a simplified AirBnB-like platform. The focus in is to create comprehensive **technical documentation** that lays the groundwork for implementation. It includes architectural design, detailed class and sequence diagrams, and entity definitions.

### Prerequisites

* Knowledge Object-Oriented Programming and UML.
* Familiarity with Mermaid.js or diagramming tools like draw.io.
* Markdown editor or IDE that supports Mermaid.js


## Deployment

This phase does not require deployment, as it focuses solely on documentation.

### Branches

* Master: Contains stable and reviewed documentation


## Diagrams

### High-Level Package Diagram

Illustrates the 3-layer architecture:
- **Presentation Layer**: APIs and services.
- **Business Logic Layer**: Models such as `User`, `Place`, `Review`, `Amenity`.
- **Persistence Layer**: Database access.

Communication uses the **Facade Pattern** for modular interaction.

### Class Diagram for Business Logic

Entities include:
- `User`: first name, last name, email, password, admin flag.
- `Place`: title, description, price, lat/lon, amenities.
- `Review`: rating, comment, references to place and user.
- `Amenity`: name, description.

All have unique IDs and timestamps for audit purposes.

### Sequence Diagrams for API Calls

Covers:
- **User Registration**
- **Place Creation**
- **Review Submission**
- **Fetching List of Places**

Each sequence diagram shows data flow across all layers: Presentation → Business Logic → Persistence.

---

By completing this phase, you ensure a solid foundation for implementing a clean, scalable architecture for HBnB Evolution.

Authors

Kamila Sostre {https://github.com/kamisos3}

Andres Mora {https://github.com/afmorac}
