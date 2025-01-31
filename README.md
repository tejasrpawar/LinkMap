# LinkMap
A tool to visualize your LinkedIn connections in an interactive network graph, helping you understand your professional network distribution.

🔗 [Demo](https://tejasrpawar.github.io/LinkMap/index.html)

## Overview
This project helps professionals understand and expand their networks by providing interactive visualization tools for LinkedIn connections.

## Features
- Interactive force-directed graph visualization
- Company-based clustering with automatic node grouping
- Dynamic zoom functionality for exploring clusters
- Interactive highlighting of company networks
- Dark theme for better visibility
- Draggable nodes for custom arrangement
- Automatic node sizing and labeling

## How It Works
1. Download your [LinkedIn connections data](https://www.linkedin.com/help/linkedin/answer/66844/export-connections-from-linkedin)
2. Upload the `connections.csv` file to the application
3. View your network visualization where:
   - Nodes represent your connections
   - Edges connect people working at the same company
   - Clusters show company groupings

## Interaction Guide
- **Click** on any node to zoom into its company cluster
- **Click** the background to reset the view
- **Drag** nodes to rearrange the network
- **Hover** over nodes to see connection details
- **Shift + Click** to reset zoom
- Unrelated nodes and connections fade when viewing a cluster

## Technical Implementation
- Built using [D3.js v4](https://d3js.org/) for force-directed graph visualization
- Custom force simulation for optimal clustering
- Smooth transitions and animations
- Responsive design that adapts to window size
- Efficient data parsing and node generation

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
- Add export functionality for the visualization
- Implement custom color themes

## References
- [D3.js v4 Force Directed Graph with Labels](https://bl.ocks.org/heybignick/3faf257bbbbc7743bb72310d03b86ee8)
- [LinkedIn Data Export Guide](https://www.linkedin.com/help/linkedin/answer/66844/export-connections-from-linkedin)

## License
This project is open source and available under the MIT License.
