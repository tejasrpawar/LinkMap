# LinkMap
A tool to visualize your LinkedIn connections in an interactive network graph, helping you understand your professional network distribution.

🔗 [Demo]()

## Overview
This project helps professionals understand and expand their networks by providing interactive visualization tools for LinkedIn connections.

## Features
- Visualize your LinkedIn connections in a force-directed graph
- Identify clusters of connections by company
- Discover potential networking opportunities
- Easy-to-use interface with interactive visualization

## How It Works
1. Download your [LinkedIn connections data](https://www.linkedin.com/help/linkedin/answer/66844/export-connections-from-linkedin)
2. Upload the `connections.csv` file to the application
3. View your network visualization where:
   - Nodes represent your connections
   - Edges connect people working at the same company

## Technical Implementation
- Built using [D3.js v4](https://d3js.org/) for force-directed graph visualization
- Parses LinkedIn's exported CSV data
- Implements custom node and edge generation algorithms

## Development Notes

### Attempted Approaches
1. **LinkedIn Official API**: Initially planned but not viable due to:
   - Limited to basic profile data for 1st-degree connections
   - API deprecated for personal use
   - Only available through LinkedIn Partnership Program

2. **Unofficial API**: Explored [linkedin_api](https://github.com/tomquirk/linkedin-api) but not implemented due to:
   - Potential violation of LinkedIn's User Agreement
   - Risk of account suspension

3. **Current Solution**: Uses LinkedIn's official data export feature
   - Compliant with LinkedIn's terms of service
   - Limited to 1st-degree connections
   - Safe and reliable approach

## Future Improvements
- Apply for LinkedIn Partnership Program for enhanced data access
- Add additional visualization options
- Implement connection strength analysis
- Add filtering and search capabilities

## References
- [D3.js v4 Force Directed Graph with Labels](https://bl.ocks.org/heybignick/3faf257bbbbc7743bb72310d03b86ee8)
- [LinkedIn Data Export Guide](https://www.linkedin.com/help/linkedin/answer/66844/export-connections-from-linkedin)

## License
This project is open source and available under the MIT License.
