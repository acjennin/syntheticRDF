#!/usr/bin/env python3
"""
Main script to generate synthetic RDF data for Schema.org/Person using rdf-graph-gen.

This script integrates custom Faker providers with SHACL shapes to generate
realistic RDF data conforming to Schema.org/Person ontology.
"""

import argparse
import sys
import random
from pathlib import Path
from rdflib import Graph, Namespace, Literal, URIRef, RDF, XSD
from rdflib.namespace import RDFS
from faker import Faker

# Import our custom provider
from providers.person_provider import SchemaOrgPersonProvider


# Define namespaces
SCHEMA = Namespace("http://schema.org/")
EX = Namespace("http://example.org/person/")


def create_person_graph(num_entities, include_deceased=False, seed=None):
    """
    Create an RDF graph with Person entities using custom Faker providers.
    
    Args:
        num_entities: Number of Person entities to generate
        include_deceased: Whether to include deceased persons (with death dates)
        seed: Random seed for reproducibility
    
    Returns:
        rdflib.Graph: RDF graph with Person data
    """
    # Initialize Faker with custom provider
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)
    
    fake = Faker()
    fake.add_provider(SchemaOrgPersonProvider)
    
    # Create graph
    g = Graph()
    g.bind("schema", SCHEMA)
    g.bind("ex", EX)
    
    print(f"Generating {num_entities} Person entities...")
    
    for i in range(num_entities):
        # Create person URI
        person_id = f"person_{i+1}"
        person_uri = EX[person_id]
        
        # Add type
        g.add((person_uri, RDF.type, SCHEMA.Person))
        
        # Determine if deceased
        is_deceased = include_deceased and random.random() < 0.1
        
        # Generate birth date first (needed for death date)
        birth_date = fake.person_birth_date()
        
        # Basic identity properties (required)
        g.add((person_uri, SCHEMA.name, Literal(fake.person_name(), datatype=XSD.string)))
        
        # Optional basic properties
        if random.random() < 0.9:
            g.add((person_uri, SCHEMA.givenName, Literal(fake.person_given_name(), datatype=XSD.string)))
        
        if random.random() < 0.9:
            g.add((person_uri, SCHEMA.familyName, Literal(fake.person_family_name(), datatype=XSD.string)))
        
        if random.random() < 0.5:
            g.add((person_uri, SCHEMA.additionalName, Literal(fake.person_additional_name(), datatype=XSD.string)))
        
        if random.random() < 0.3:
            g.add((person_uri, SCHEMA.alternateName, Literal(fake.person_alternate_name(), datatype=XSD.string)))
        
        if random.random() < 0.6:
            g.add((person_uri, SCHEMA.honorificPrefix, Literal(fake.person_honorific_prefix(), datatype=XSD.string)))
        
        if random.random() < 0.2:
            g.add((person_uri, SCHEMA.honorificSuffix, Literal(fake.person_honorific_suffix(), datatype=XSD.string)))
        
        # Contact information
        if random.random() < 0.8:
            g.add((person_uri, SCHEMA.email, Literal(fake.person_email(), datatype=XSD.string)))
        
        if random.random() < 0.7:
            g.add((person_uri, SCHEMA.telephone, Literal(fake.person_telephone(), datatype=XSD.string)))
        
        if random.random() < 0.2:
            g.add((person_uri, SCHEMA.faxNumber, Literal(fake.person_fax_number(), datatype=XSD.string)))
        
        if random.random() < 0.4:
            g.add((person_uri, SCHEMA.url, Literal(fake.person_url(), datatype=XSD.anyURI)))
        
        # Biographical information
        g.add((person_uri, SCHEMA.birthDate, Literal(birth_date, datatype=XSD.date)))
        
        if random.random() < 0.5:
            g.add((person_uri, SCHEMA.birthPlace, Literal(fake.person_birth_place(), datatype=XSD.string)))
        
        if is_deceased:
            death_date = fake.person_death_date(birth_date)
            g.add((person_uri, SCHEMA.deathDate, Literal(death_date, datatype=XSD.date)))
            g.add((person_uri, SCHEMA.deathPlace, Literal(fake.person_death_place(), datatype=XSD.string)))
        
        g.add((person_uri, SCHEMA.gender, Literal(fake.person_gender(), datatype=XSD.string)))
        
        if random.random() < 0.7:
            g.add((person_uri, SCHEMA.nationality, Literal(fake.person_nationality(), datatype=XSD.string)))
        
        # Professional information
        if random.random() < 0.8:
            g.add((person_uri, SCHEMA.jobTitle, Literal(fake.person_job_title(), datatype=XSD.string)))
        
        if random.random() < 0.7:
            g.add((person_uri, SCHEMA.worksFor, Literal(fake.person_works_for(), datatype=XSD.string)))
        
        if random.random() < 0.4:
            g.add((person_uri, SCHEMA.affiliation, Literal(fake.person_affiliation(), datatype=XSD.string)))
        
        if random.random() < 0.6:
            g.add((person_uri, SCHEMA.alumniOf, Literal(fake.person_alumni_of(), datatype=XSD.string)))
        
        # Physical characteristics
        if random.random() < 0.3:
            g.add((person_uri, SCHEMA.height, Literal(fake.person_height(), datatype=XSD.string)))
        
        if random.random() < 0.2:
            g.add((person_uri, SCHEMA.weight, Literal(fake.person_weight(), datatype=XSD.string)))
        
        # Address (create as separate node)
        if random.random() < 0.6:
            address_data = fake.person_address()
            address_uri = EX[f"{person_id}_address"]
            
            g.add((person_uri, SCHEMA.address, address_uri))
            g.add((address_uri, RDF.type, SCHEMA.PostalAddress))
            g.add((address_uri, SCHEMA.streetAddress, Literal(address_data["streetAddress"], datatype=XSD.string)))
            g.add((address_uri, SCHEMA.addressLocality, Literal(address_data["addressLocality"], datatype=XSD.string)))
            g.add((address_uri, SCHEMA.addressRegion, Literal(address_data["addressRegion"], datatype=XSD.string)))
            g.add((address_uri, SCHEMA.postalCode, Literal(address_data["postalCode"], datatype=XSD.string)))
            g.add((address_uri, SCHEMA.addressCountry, Literal(address_data["addressCountry"], datatype=XSD.string)))
        
        # Social and recognition
        if random.random() < 0.3:
            g.add((person_uri, SCHEMA.award, Literal(fake.person_award(), datatype=XSD.string)))
        
        if random.random() < 0.5:
            languages = fake.person_knows_language()
            if isinstance(languages, list):
                for lang in languages:
                    g.add((person_uri, SCHEMA.knowsLanguage, Literal(lang, datatype=XSD.string)))
            else:
                g.add((person_uri, SCHEMA.knowsLanguage, Literal(languages, datatype=XSD.string)))
        
        # Identifiers
        if random.random() < 0.5:
            g.add((person_uri, SCHEMA.taxID, Literal(fake.person_tax_id(), datatype=XSD.string)))
        
        if random.random() < 0.2:
            g.add((person_uri, SCHEMA.vatID, Literal(fake.person_vat_id(), datatype=XSD.string)))
        
        # Progress indicator
        if (i + 1) % 10 == 0:
            print(f"  Generated {i + 1}/{num_entities} persons...")
    
    print(f"✓ Successfully generated {num_entities} Person entities")
    return g


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Generate synthetic RDF data for Schema.org/Person entities",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate 100 persons and save to file
  python generate_person_data.py --num-entities 100 --output persons.ttl
  
  # Generate with deceased persons included
  python generate_person_data.py --num-entities 50 --include-deceased --output persons.ttl
  
  # Use a specific random seed for reproducibility
  python generate_person_data.py --num-entities 100 --seed 42 --output persons.ttl
  
  # Output in different RDF formats
  python generate_person_data.py --num-entities 100 --output persons.rdf --format xml
  python generate_person_data.py --num-entities 100 --output persons.jsonld --format json-ld
        """
    )
    
    parser.add_argument(
        "--num-entities",
        type=int,
        default=10,
        help="Number of Person entities to generate (default: 10)"
    )
    
    parser.add_argument(
        "--output",
        type=str,
        default="output_persons.ttl",
        help="Output file path (default: output_persons.ttl)"
    )
    
    parser.add_argument(
        "--format",
        type=str,
        default="turtle",
        choices=["turtle", "xml", "n3", "nt", "json-ld"],
        help="Output RDF format (default: turtle)"
    )
    
    parser.add_argument(
        "--include-deceased",
        action="store_true",
        help="Include some deceased persons with death dates/places"
    )
    
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Random seed for reproducibility"
    )
    
    parser.add_argument(
        "--print-stats",
        action="store_true",
        help="Print statistics about the generated graph"
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.num_entities <= 0:
        print("Error: num-entities must be positive", file=sys.stderr)
        return 1
    
    try:
        # Generate the graph
        print(f"\nSchema.org Person Data Generator")
        print("=" * 60)
        print(f"Configuration:")
        print(f"  Entities: {args.num_entities}")
        print(f"  Output: {args.output}")
        print(f"  Format: {args.format}")
        print(f"  Include deceased: {args.include_deceased}")
        if args.seed is not None:
            print(f"  Random seed: {args.seed}")
        print()
        
        graph = create_person_graph(
            num_entities=args.num_entities,
            include_deceased=args.include_deceased,
            seed=args.seed
        )
        
        # Save to file
        print(f"\nSaving to {args.output}...")
        graph.serialize(destination=args.output, format=args.format)
        print(f"✓ Successfully saved to {args.output}")
        
        # Print statistics if requested
        if args.print_stats:
            print("\nGraph Statistics:")
            print("-" * 60)
            print(f"  Total triples: {len(graph)}")
            print(f"  Person entities: {args.num_entities}")
            print(f"  Avg triples per person: {len(graph) / args.num_entities:.1f}")
            
            # Count properties
            properties = {}
            for s, p, o in graph:
                prop_name = str(p).replace(str(SCHEMA), "schema:")
                properties[prop_name] = properties.get(prop_name, 0) + 1
            
            print(f"\n  Property usage:")
            for prop, count in sorted(properties.items(), key=lambda x: x[1], reverse=True)[:10]:
                print(f"    {prop}: {count}")
        
        print("\n" + "=" * 60)
        print("Generation complete!")
        
        return 0
        
    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())



