### Activity: **Social Coding Portfolio Setup via Command Line**

**Objective:**  
This activity is designed to help you set up your social coding portfolio using the command line or terminal. You’ll organize the various components of your portfolio, which will include datasets, scripts, notebooks, and reflections. The goal is to streamline your workflow for the course and create a well-structured, easily navigable portfolio.

**Instructions:**

1. **Creating a Social Coding Portfolio Directory:**
   - Open your terminal and navigate to your home directory or wherever you prefer to keep your projects:
     ```bash
     cd ~/desktop
     ```
   - Create a main directory for your social coding portfolio:
     ```bash
     mkdir Social_Coding_Portfolio
     ```
   - Navigate into your new portfolio directory:
     ```bash
     cd Social_Coding_Portfolio
     ```

2. **Creating Subdirectories for Portfolio Organization:**
   
   - Within your main directory, create subdirectories to organize the different components of your portfolio. You should create folders for activities, final projects, notebooks, and reflections:
     ```bash
     mkdir Activities Final_Project Reflections 
     ```
   
3. **Creating and Naming Files:**
   - Inside each subdirectory, create placeholder files that represent the types of files you’ll be working with throughout the course:
     - For example, in the `Activities` folder, create files for each programming activity:
       ```bash
       touch Activities/activity1.ipynb Activities/activity2.ipynb
       ```
     - In the `Reflections` folder, create markdown files for your reflective writing:
       ```bash
       touch Reflections/activity1_reflection.md Reflections/activity2_reflection.md
       ```

4. **Moving Files Between Directories:**
   - If you decide to reorganize your files, use the `mv` command. For example, if you initially placed a notebook in the wrong folder:
     ```bash
     mv Notebooks/activity1.ipynb Activities/
     ```

5. **Renaming Files:**
   - If you need to rename a file to better reflect its content or purpose, do so with the `mv` command:
     ```bash
     mv Activities/activity1.ipynb Activities/data_cleaning_activity.ipynb
     ```

6. **Listing Directory Contents:**
   - To check the organization of your portfolio, list the contents of your main directory and its subdirectories:
     ```bash
     ls
     ls Activities/
     ls Reflections/
     ```

7. **Deleting Files or Directories:**
   - If you need to remove unnecessary files or directories, use the `rm` command. For example, delete a placeholder file you no longer need:
     ```bash
     rm Final_Project/old_project_notes.md
     rm -r Notebooks/unused_notebooks
     ```

8. **Listing the Path to Your Portfolio Directory:**
   
   - Display the full path to your portfolio directory. This can be useful when setting up your repository or sharing your work with others:
     ```bash
     pwd
     ```
   
   
